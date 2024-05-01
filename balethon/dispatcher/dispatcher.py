from asyncio import get_event_loop, new_event_loop
from concurrent.futures import ThreadPoolExecutor

from .print_chain import print_chain
from .log_chain import log_chain
from ..errors import ContinueDispatching, BreakDispatching


def is_subclass(cls, super_cls):
    if not isinstance(cls, type):
        return False
    return issubclass(cls, super_cls)


class Dispatcher:

    def __init__(self, max_workers: int = None):
        self.chains = [print_chain, log_chain]
        try:
            self.event_loop = get_event_loop()
        except RuntimeError:
            self.event_loop = new_event_loop()
        self.thread_pool_executor = ThreadPoolExecutor(max_workers, thread_name_prefix="Event Handler")

    async def __call__(self, client, event):
        for chain in self.chains:
            if not await chain.check(client, event):
                continue
            for event_handler in chain.event_handlers:
                if not isinstance(event, event_handler.can_handle) and not is_subclass(event, event_handler.can_handle):
                    continue
                try:
                    if await event_handler.check(client, event):
                        await event_handler(client=client, event=event)
                        break
                except ContinueDispatching:
                    break
                except BreakDispatching:
                    return
                except Exception as error:
                    await self(client, error)

    def add_chain(self, chain):
        self.chains.append(chain)

    def get_chain(self, name):
        for chain in self.chains:
            if chain.name == name:
                return chain
        raise ValueError(f"Chain \"{name}\" does not exist")

    def del_chain(self, name):
        for i, chain in enumerate(self.chains):
            if chain.name == name:
                del self.chains[i]
        raise ValueError(f"Chain \"{name}\" does not exist")
