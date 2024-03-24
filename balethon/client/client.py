from json import dumps
from asyncio import get_event_loop
from inspect import iscoroutine, iscoroutinefunction
from io import BufferedReader
from asyncio import CancelledError

from httpx import ConnectError

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
from ..event_handlers import ConnectHandler, DisconnectHandler, InitializeHandler, ShutdownHandler
from ..smart_call import remove_unwanted_keyword_parameters


# TODO: adding a decorator for creating methods
class Client(Messages, Updates, Users, Attachments, Chats, Payments, Stickers, EventHandlers):

    def __init__(
            self,
            token: str,
            max_workers: int = None,
            time_out: int = None,
            proxies=None,
            base_url: str = None,
            short_url: str = None
    ):
        self.dispatcher = Dispatcher(max_workers)
        self.connection = Connection(token, time_out, proxies, base_url, short_url)
        self.user = None
        self.is_disconnected = False
        self.is_initialized = False

    def __repr__(self):
        client_name = type(self).__name__
        try:
            name = self.user.full_name
        except AttributeError:
            name = "Not initialized yet"
        return f"{client_name}({name})"

    async def connect(self):
        await self.connection.start()
        await self.dispatcher(self, ConnectHandler)
        self.user = await self.get_me()

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

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        try:
            self.disconnect()
        except ConnectionError:
            return

    async def execute(self, method: str, service: str, json: bool = True, **data):
        data = {k: v for k, v in data.items() if v is not None}
        files = {}
        if not json:
            for key, value in data.copy().items():
                if isinstance(value, (bytes, BufferedReader)):
                    files[key] = value
                    del data[key]
                elif isinstance(value, dict):
                    data[key] = dumps(value)
        if json:
            return await self.connection.request(method, service, json=data, files=files)
        return await self.connection.request(method, service, data=data, files=files)

    async def initialize(self):
        if self.is_initialized:
            raise ConnectionError("Dispatcher is already started")
        self.is_initialized = True
        await self.dispatcher(self, InitializeHandler)

    async def shutdown(self):
        if not self.is_initialized:
            raise ConnectionError("Dispatcher is already stopped")
        self.is_initialized = False
        await self.dispatcher(self, ShutdownHandler)

    async def start_polling(self):
        try:
            await self.delete_webhook()
            await self.initialize()
            last_update_id = None
            while True:
                try:
                    if last_update_id is None:
                        updates = await self.get_updates()
                        if updates:
                            last_update_id = updates[-1].id
                    else:
                        updates = await self.get_updates(last_update_id + 1)
                except ConnectError:
                    if not self.is_disconnected:
                        self.is_disconnected = True
                        await self.dispatcher(self, DisconnectHandler)
                except Exception as error:
                    await self.dispatcher(self, error)
                else:
                    if self.is_disconnected:
                        self.is_disconnected = False
                        await self.dispatcher(self, ConnectHandler)
                    for update in updates:
                        if last_update_id is not None and last_update_id >= update.id:
                            continue
                        last_update_id = update.id
                        await self.dispatcher(self, update.available_update)
        except CancelledError:
            await self.shutdown()

    def run(self, function=None):
        try:
            self.connect()
            if function is None:
                self.start_polling()
            elif iscoroutine(function):
                loop = get_event_loop()
                loop.run_until_complete(function)
            elif iscoroutinefunction(function):
                kwargs = remove_unwanted_keyword_parameters(function, client=self)
                loop = get_event_loop()
                loop.run_until_complete(function(**kwargs))
            else:
                kwargs = remove_unwanted_keyword_parameters(function, client=self)
                function(**kwargs)
        except KeyboardInterrupt:
            if self.is_initialized:
                self.shutdown()
            return
        finally:
            self.disconnect()

    async def download(self, file_id: str):
        return await self.connection.download_file(file_id)

    async def resolve_peer_id(self, chat_id):
        if isinstance(chat_id, str) and not chat_id.isnumeric():
            peer = await self.get_chat(chat_id)
            return peer.id
        return chat_id

    def create_deep_link(self, referral_parameter: str) -> str:
        return f"{self.connection.short_url}/{self.user.username}?{referral_parameter}"
