from .types import Message, CallbackQuery
from .handlers import MessageHandler, CallbackQueryHandler


class Dispatcher:

    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    async def __call__(self, client, update):
        for handler in self.handlers:
            if update.get("message") and isinstance(handler, MessageHandler):
                message = Message.from_dict(client, update["message"])
                if await handler.check(client, message):
                    await handler(client, message)
            elif update.get("callback_query") and isinstance(handler, CallbackQueryHandler):
                callback_query = CallbackQuery.from_dict(client, update["callback_query"])
                if await handler.check(client, callback_query):
                    await handler(client, callback_query)
