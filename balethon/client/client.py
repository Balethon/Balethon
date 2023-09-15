from asyncio import get_event_loop

from .messages import Messages
from .updates import Updates
from .users import Users
from .attachments import Attachments
from .chats import Chats
from .payments import Payments
from ..network import Connection
from ..dispatcher import Dispatcher
from ..event_handlers import (
    EventHandler,
    UpdateHandler,
    ErrorHandler,
    MessageHandler,
    CallbackQueryHandler,
    CommandHandler
)


# TODO: adding a decorator for creating methods
class Client(Messages, Updates, Users, Attachments, Chats, Payments):

    def __init__(self, token, time_out=20):
        self.connection = Connection(token, time_out)
        self.dispatcher = Dispatcher()

    def __repr__(self):
        name = type(self).__name__
        return f"{name}({self.connection.token})"

    async def connect(self):
        await self.connection.start()

    async def disconnect(self):
        await self.connection.stop()

    async def __aenter__(self):
        await self.connect()
        return self

    async def __aexit__(self, *args):
        try:
            await self.disconnect()
        except ConnectionError:
            return

    def add_event_handler(self, event_handler):
        self.dispatcher.add_event_handler(event_handler)

    def remove_event_handler(self, event_handler):
        self.dispatcher.remove_event_handler(event_handler)

    def on_event(self, condition=None):
        def decorator(callback):
            self.add_event_handler(EventHandler(callback, condition))
            return callback
        return decorator

    def on_error(self, condition=None):
        def decorator(callback):
            self.add_event_handler(ErrorHandler(callback, condition))
            return callback
        return decorator

    def on_update(self, condition=None):
        def decorator(callback):
            self.add_event_handler(UpdateHandler(callback, condition))
            return callback
        return decorator

    def on_message(self, condition=None):
        def decorator(callback):
            self.add_event_handler(MessageHandler(callback, condition))
            return callback
        return decorator

    def on_callback_query(self, condition=None):
        def decorator(callback):
            self.add_event_handler(CallbackQueryHandler(callback, condition))
            return callback
        return decorator

    def on_command(self, condition=None, name=None):
        def decorator(callback):
            self.add_event_handler(CommandHandler(callback, condition, name))
            return callback
        return decorator

    async def start_polling(self):
        seen = [u.id for u in (await self.get_updates())]
        while True:
            updates = await self.get_updates()
            for update in updates:
                if update.id in seen:
                    continue
                seen.append(update.id)
                update = update.available_update
                await self.dispatcher(self, update)

    def run(self, func):
        loop = get_event_loop()
        try:
            loop.run_until_complete(self.connect())
            loop.run_until_complete(func)
        except KeyboardInterrupt:
            return
        finally:
            loop.run_until_complete(self.disconnect())

    def run_polling(self):
        self.run(self.start_polling())
