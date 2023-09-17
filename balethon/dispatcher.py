from asyncio import create_task

from .event_handlers import ErrorHandler


async def show_error(client, error):
    print(error)


class Dispatcher:

    def __init__(self):
        self.event_handlers = []
        self.tasks = []
        self.add_event_handler(ErrorHandler(show_error))

    def add_event_handler(self, event_handler):
        self.event_handlers.append(event_handler)

    def remove_event_handler(self, event_handler):
        self.event_handlers.remove(event_handler)

    @staticmethod
    async def dispatch(client, event, event_handler):
        if await event_handler.check(client, event):
            await event_handler(client, event)

    async def __call__(self, client, event):
        for event_handler in self.event_handlers:
            try:
                if not isinstance(event, event_handler.can_handle):
                    continue
                self.tasks.append(create_task(self.dispatch(client, event, event_handler)))
            except Exception as error:
                await self(client, error)
