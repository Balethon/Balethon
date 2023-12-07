from asyncio import get_event_loop, new_event_loop
from concurrent.futures import ThreadPoolExecutor
from traceback import print_exception

from .event_handlers import ErrorHandler
from .errors import ContinueDispatching, BreakDispatching


async def print_error(client, error):
    print_exception(None, error, error.__traceback__)


class Dispatcher:

    def __init__(self, max_workers: int = None):
        self.event_handler_chains: dict = {}
        self.add_event_handler(ErrorHandler(print_error), chain="print_error")
        try:
            self.event_loop = get_event_loop()
        except RuntimeError:
            self.event_loop = new_event_loop()
        self.thread_pool_executor = ThreadPoolExecutor(max_workers, "Event Handler")

    def add_event_handler(self, event_handler, chain="default"):
        if chain not in self.event_handler_chains:
            self.event_handler_chains[chain] = []
        self.event_handler_chains[chain].append(event_handler)

    def remove_event_handler(self, event_handler):
        for name, event_handler_chain in self.event_handler_chains.items():
            try:
                event_handler_chain.remove(event_handler)
            except ValueError:
                continue
            else:
                if not event_handler_chain:
                    del self.event_handler_chains[name]
                return
        raise ValueError(f"{event_handler} does not exist")

    async def __call__(self, client, event):
        for event_handler_chain in self.event_handler_chains.values():
            for event_handler in event_handler_chain:
                if not isinstance(event, event_handler.can_handle):
                    continue
                try:
                    if await event_handler.check(client, event):
                        await event_handler(client, event)
                        break
                except ContinueDispatching:
                    break
                except BreakDispatching:
                    return
                except Exception as error:
                    await self(client, error)
