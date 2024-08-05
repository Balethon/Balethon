from asyncio import get_event_loop, new_event_loop, Queue
from concurrent.futures import ThreadPoolExecutor
from os import cpu_count

from .chain import Chain
from ..errors import ContinueDispatching, BreakDispatching
from ..event_handlers import EventHandler
from ..objects import Update


def is_subclass(cls, super_cls):
    if not isinstance(cls, type):
        return False
    return issubclass(cls, super_cls)


class Dispatcher:
    reasonable_sync_workers = min(32, (cpu_count() or 1) + 4)
    reasonable_async_workers = reasonable_sync_workers * 5

    def __init__(
            self,
            *clients,
            async_workers: int = None,
            sync_workers: int = None
    ):
        self.clients = clients
        try:
            self.event_loop = get_event_loop()
        except RuntimeError:
            self.event_loop = new_event_loop()
        self.events_queue = Queue()
        self.is_started = False
        self.async_workers_count = self.reasonable_async_workers or async_workers
        self.async_workers = []
        self.sync_workers_count = self.reasonable_sync_workers or sync_workers
        self.sync_workers = None

    async def start(self):
        if self.is_started:
            raise RuntimeError("Dispatcher is already started")
        self.is_started = True
        self.async_workers = [self.event_loop.create_task(self.worker()) for _ in range(self.async_workers_count)]
        self.sync_workers = ThreadPoolExecutor(self.sync_workers_count, thread_name_prefix="Event Handler")

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Dispatcher is already stopped")
        self.is_started = False
        for _ in self.async_workers:
            self.events_queue.put_nowait(None)
        for async_worker in self.async_workers:
            await async_worker
        self.async_workers.clear()
        self.sync_workers.shutdown()

    async def propagate_chain(self, chain, client, event):
        for child in chain.children:
            if isinstance(child, Chain):
                if not await child.check(client, event):
                    continue
                await self.propagate_chain(child, client, event)
                break
            elif isinstance(child, EventHandler):
                if not isinstance(event, child.can_handle) and not is_subclass(event, child.can_handle):
                    continue
                try:
                    if not await child.check(client, event):
                        continue
                    await child(client=client, event=event)
                    break
                except ContinueDispatching:
                    continue
                except BreakDispatching:
                    break
                except Exception as error:
                    await self.dispatch_event(client, error)
        for child in chain.chains:
            if not await child.check(client, event):
                continue
            await self.propagate_chain(child, client, event)

    async def worker(self):
        while True:
            item = await self.events_queue.get()
            if item is None:
                break
            client, event = item
            await self.propagate_chain(client, client, event)

    async def dispatch_event(self, client, event):
        if self.is_started:
            self.events_queue.put_nowait((client, event))

    async def dispatch_raw_update(self, client, update):
        update = Update.wrap(update).get_effective_update()
        update.bind(client)
        await self.dispatch_event(client, update)
