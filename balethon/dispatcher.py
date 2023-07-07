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
            if "message" in update.keys() and isinstance(handler, MessageHandler):
                message = update["message"]
                await handler.callback(client, message)
            elif "callback_query" in update.keys() and isinstance(handler, CallbackQueryHandler):
                callback_query = update["callback_query"]
                await handler.callback(client, callback_query)
