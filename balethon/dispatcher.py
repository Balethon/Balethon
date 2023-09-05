class Dispatcher:

    def __init__(self):
        self.event_handlers = []

    def add_event_handler(self, event_handler):
        self.event_handlers.append(event_handler)

    def remove_event_handler(self, event_handler):
        self.event_handlers.remove(event_handler)

    async def __call__(self, client, update):
        update = update.available_update
        for event_handler in self.event_handlers:
            if not isinstance(update, event_handler.can_handle):
                continue
            if await event_handler.check(client, update):
                await event_handler(client, update)
