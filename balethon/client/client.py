from asyncio import get_event_loop
from inspect import iscoroutine
from io import BufferedReader

from .messages import Messages
from .updates import Updates
from .users import Users
from .attachments import Attachments
from .chats import Chats
from .payments import Payments
from .stickers import Stickers
from .event_handlers import EventHandlers
from ..network import Connection
from ..dispatcher import Dispatcher
from ..event_handlers import ConnectHandler, DisconnectHandler


# TODO: adding a decorator for creating methods
class Client(Messages, Updates, Users, Attachments, Chats, Payments, Stickers, EventHandlers):

    def __init__(self, token, time_out=None, base_url=None, short_url=None):
        self.connection = Connection(token, time_out, base_url, short_url)
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

    async def execute(self, method, service, json=True, **data):
        data = {k: v for k, v in data.items() if v is not None}
        files = {}
        for key, value in data.copy().items():
            if isinstance(value, (bytes, BufferedReader)):
                files[key] = value
                del data[key]
        if json:
            return await self.connection.request(method, service, json=data, files=files)
        return await self.connection.request(method, service, data=data, files=files)

    async def start_polling(self):
        await self.delete_webhook()
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

    async def resolve_peer_id(self, chat_id):
        if isinstance(chat_id, str) and chat_id.startswith("@"):
            peer = await self.get_chat(chat_id)
            return peer.id
        return chat_id

    def create_deep_link(self, referral_parameter):
        return f"{self.connection.short_url}/{self.user.username}?{referral_parameter}"
