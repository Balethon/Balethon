from .event_handlers import MessageEventHandler, CallbackQueryEventHandler


class Dispatcher:

    def __init__(self):
        self.event_handlers = []

    def add_event_handler(self, handler):
        self.event_handlers.append(handler)

    def remove_event_handler(self, handler):
        self.event_handlers.remove(handler)

    async def __call__(self, client, update):
        for handler in self.event_handlers:
            if update.get("message") and isinstance(handler, MessageEventHandler):
                message = update["message"]
                if await handler.check(client, message):
                    await handler(client, message)
            elif update.get("callback_query") and isinstance(handler, CallbackQueryEventHandler):
                callback_query = update["callback_query"]
                if await handler.check(client, callback_query):
                    await handler(client, callback_query)
