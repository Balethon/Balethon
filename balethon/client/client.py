from asyncio import get_event_loop
from inspect import iscoroutine

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
    ConnectHandler,
    DisconnectHandler,
    UpdateHandler,
    ErrorHandler,
    MessageHandler,
    CallbackQueryHandler,
    CommandHandler,
    ShippingQueryHandler,
    PreCheckoutQueryHandler
)


# TODO: adding a decorator for creating methods
class Client(Messages, Updates, Users, Attachments, Chats, Payments):

    def __init__(self, token, time_out=20):
        self.connection = Connection(token, time_out)
        self.dispatcher = Dispatcher()
        self.user = None

    def __repr__(self):
        name = type(self).__name__
        return f"{name}({self.connection.token})"

    async def connect(self):
        await self.connection.start()
        self.user = await self.get_me()
        await self.dispatcher(self, ConnectHandler)

    async def disconnect(self):
        await self.connection.stop()
        await self.dispatcher(self, DisconnectHandler)

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

    def add(self, event_handler_type, *args, **kwargs):
        def decorator(callback):
            self.add_event_handler(event_handler_type(callback, *args, **kwargs))
            return callback
        return decorator

    def on_event(self, condition=None):
        def decorator(callback):
            self.add_event_handler(EventHandler(callback, condition))
            return callback
        return decorator

    def on_connect(self):
        def decorator(callback):
            self.add_event_handler(ConnectHandler(callback))
            return callback
        return decorator

    def on_disconnect(self):
        def decorator(callback):
            self.add_event_handler(DisconnectHandler(callback))
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

    def on_shipping_query(self, condition=None):
        def decorator(callback):
            self.add_event_handler(ShippingQueryHandler(callback, condition))
            return callback
        return decorator

    def on_pre_checkout_query(self, condition=None):
        def decorator(callback):
            self.add_event_handler(PreCheckoutQueryHandler(callback, condition))
            return callback
        return decorator

    async def start_polling(self):
        last_update_id = None
        first_time = True
        while True:
            try:
                if last_update_id is None:
                    updates = await self.get_updates()
                    if first_time:
                        if updates:
                            last_update_id = updates[-1].id
                        first_time = False
                        continue
                else:
                    updates = await self.get_updates(last_update_id + 1)
            except Exception as error:
                await self.dispatcher(self, error)
            else:
                for update in updates:
                    last_update_id = update.id
                    await self.dispatcher(self, update.available_update)

    def run(self, function):
        loop = get_event_loop()
        try:
            loop.run_until_complete(self.connect())
            if iscoroutine(function):
                loop.run_until_complete(function)
            else:
                function()
        except KeyboardInterrupt:
            return
        finally:
            loop.run_until_complete(self.disconnect())

    def run_polling(self):
        self.run(self.start_polling())

    async def download(self, file_id):
        return await self.connection.download_file(file_id)
