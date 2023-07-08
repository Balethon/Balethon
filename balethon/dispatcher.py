from .types import Message, CallbackQuery
from .handlers import MessageHandler, CallbackQueryHandler


class Dispatcher:

    def __init__(self):
        self.handlers = []

    def add_handler(self, handler):
        self.handlers.append(handler)

    def remove_handler(self, handler):
        self.handlers.remove(handler)

    async def dispatch(self, client, update):
        for handler in self.handlers:
            if update.get("message") and isinstance(handler, MessageHandler):
                message = Message.from_dict(client, update["message"])
                await handler.callback(client, message)
            elif update.get("callback_query") and isinstance(handler, CallbackQueryHandler):
                callback_query = CallbackQuery.from_dict(client, update["callback_query"])
                await handler.callback(client, callback_query)
