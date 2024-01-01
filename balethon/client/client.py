from asyncio import get_event_loop
from inspect import iscoroutine, iscoroutinefunction
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
from ..event_handlers import ConnectHandler, DisconnectHandler, ErrorHandler
from ..smart_call import remove_unwanted_parameters


# TODO: adding a decorator for creating methods
class Client(Messages, Updates, Users, Attachments, Chats, Payments, Stickers, EventHandlers):

    def __init__(
            self,
            token: str,
            max_workers: int = None,
            time_out: int = None,
            base_url: str = None,
            short_url: str = None
    ):
        self.dispatcher = Dispatcher(max_workers)
        self.connection = Connection(token, time_out, base_url, short_url)
        self.user = None

    def __repr__(self):
        name = type(self).__name__
        return f"{name}({self.connection.token})"

    async def connect(self):
        await self.connection.start()
        await self.dispatcher(self, None, ConnectHandler)
        self.user = await self.get_me()

    async def disconnect(self):
        await self.connection.stop()
        await self.dispatcher(self, None, DisconnectHandler)

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
        while True:
            try:
                if last_update_id is None:
                    updates = await self.get_updates(-1)
                    if updates:
                        last_update_id = updates[-1].id
                else:
                    updates = await self.get_updates(last_update_id + 1)
            except Exception as error:
                await self.dispatcher(self, error, ErrorHandler)
            else:
                for update in updates:
                    if last_update_id is not None and last_update_id >= update.id:
                        continue
                    last_update_id = update.id
                    await self.dispatcher(self, update.available_update, update.available_update_event_handler_type)

    def run(self, function=None):
        try:
            self.connect()
            if function is None:
                self.start_polling()
            elif iscoroutine(function):
                loop = get_event_loop()
                loop.run_until_complete(function)
            elif iscoroutinefunction(function):
                kwargs = remove_unwanted_parameters(function, client=self)
                loop = get_event_loop()
                loop.run_until_complete(function(**kwargs))
            else:
                kwargs = remove_unwanted_parameters(function, client=self)
                function(**kwargs)
        except KeyboardInterrupt:
            return
        finally:
            self.disconnect()

    async def download(self, file_id: str) -> str:
        return await self.connection.download_file(file_id)

    async def resolve_peer_id(self, chat_id):
        if isinstance(chat_id, str) and not chat_id.isnumeric():
            peer = await self.get_chat(chat_id)
            return peer.id
        return chat_id

    def create_deep_link(self, referral_parameter: str) -> str:
        return f"{self.connection.short_url}/{self.user.username}?{referral_parameter}"
