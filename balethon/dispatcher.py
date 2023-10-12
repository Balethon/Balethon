from traceback import print_exception
from asyncio import create_task

from .event_handlers import ErrorHandler


async def show_error(client, error):
    print_exception(error)


class Dispatcher:

    def __init__(self):
        self.event_handlers = []
        self.tasks = []
        self.add_event_handler(ErrorHandler(show_error))

    def add_event_handler(self, event_handler):
        self.event_handlers.append(event_handler)

    def remove_event_handler(self, event_handler):
        self.event_handlers.remove(event_handler)

    async def dispatch(self, client, event, event_handler):
        try:
            if await event_handler.check(client, event):
                await event_handler(client, event)
        except Exception as error:
            await self(client, error)

    async def __call__(self, client, event):
        for event_handler in self.event_handlers:
            if not isinstance(event, event_handler.can_handle):
                continue
            task = create_task(self.dispatch(client, event, event_handler))
            self.tasks.append(task)
