from .event_handlers import MessageHandler, CallbackQueryHandler, CommandHandler


class Dispatcher:

    def __init__(self):
        self.event_handlers = []

    def add_event_handler(self, event_handler):
        self.event_handlers.append(event_handler)

    def remove_event_handler(self, event_handler):
        self.event_handlers.remove(event_handler)

    async def __call__(self, client, update):
        for event_handler in self.event_handlers:
            if update.get("message") and isinstance(event_handler, (MessageHandler, CommandHandler)):
                message = update["message"]
                if await event_handler.check(client, message):
                    await event_handler(client, message)
            elif update.get("callback_query") and isinstance(event_handler, CallbackQueryHandler):
                callback_query = update["callback_query"]
                if await event_handler.check(client, callback_query):
                    await event_handler(client, callback_query)
