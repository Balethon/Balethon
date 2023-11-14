from traceback import print_exception
from asyncio import create_task

from .event_handlers import ErrorHandler
from .errors import ContinueDispatching, BreakDispatching


async def print_error(client, error):
    print_exception(None, error, error.__traceback__)


class Dispatcher:

    def __init__(self):
        self.event_handler_chains = {}
        self.add_event_handler(ErrorHandler(print_error), chain="print_error")

    def add_event_handler(self, event_handler, chain="default"):
        if chain not in self.event_handler_chains:
            self.event_handler_chains[chain] = []
        self.event_handler_chains[chain].append(event_handler)

    def remove_event_handler(self, event_handler):
        for event_handler_chain in self.event_handler_chains:
            try:
                event_handler_chain.remove(event_handler)
            except ValueError:
                continue
            else:
                break

    async def __call__(self, client, event):
        for event_handler_chain in self.event_handler_chains.values():
            for event_handler in event_handler_chain:
                if not isinstance(event, event_handler.can_handle):
                    continue
                try:
                    if await event_handler.check(client, event):
                        await create_task(event_handler(client, event))
                        break
                except ContinueDispatching:
                    break
                except BreakDispatching:
                    return
                except Exception as error:
                    await self(client, error)
