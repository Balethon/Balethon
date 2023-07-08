from .types import Message
from .types.chats.user import User
from .types.chats.chat import Chat
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
                update["message"]["from"] = User.from_dict(update["message"]["from"])
                update["message"]["forward_from"] = User.from_dict(update["message"]["forward_from"])
                update["message"]["chat"] = Chat.from_dict(update["message"]["chat"])
                update["message"]["forward_from_chat"] = Chat.from_dict(update["message"]["forward_from_chat"])
                
                message = Message.from_dict(update["message"])
                await handler.callback(client, message)
            elif update.get("callback_query") and isinstance(handler, CallbackQueryHandler):
                callback_query = update["callback_query"]
                await handler.callback(client, callback_query)
