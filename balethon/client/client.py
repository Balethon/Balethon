from json import dumps
from asyncio import get_event_loop, CancelledError, sleep
from inspect import iscoroutine, iscoroutinefunction
from io import BufferedReader

from httpx import ConnectError

from .messages import Messages
from .updates import Updates
from .users import Users
from .attachments import Attachments
from .chats import Chats
from .payments import Payments
from .stickers import Stickers
from ..errors import TooManyRequestsError
from ..network import Connection
from ..dispatcher import Dispatcher, Chain, print_chain, log_chain
from ..event_handlers import ConnectHandler, DisconnectHandler, InitializeHandler, ShutdownHandler
from ..smart_call import remove_unwanted_keyword_parameters


class Client(Chain, Messages, Updates, Users, Attachments, Chats, Payments, Stickers):

    def __init__(
            self,
            token: str,
            async_workers: int = None,
            sync_workers: int = None,
            time_out: int = None,
            sleep_threshold: int = 60,
            proxies=None,
            base_url: str = None,
            short_url: str = None
    ):
        super().__init__("default", None, print_chain, log_chain)
        self.dispatcher = Dispatcher(self, async_workers=async_workers, sync_workers=sync_workers)
        self.connection = Connection(token, time_out, proxies, base_url, short_url)
        self.sleep_threshold = sleep_threshold
        self.user = None
        self.is_disconnected = False

    def __repr__(self):
        client_name = type(self).__name__
        try:
            name = self.user.full_name
        except AttributeError:
            name = "Not initialized yet"
        return f"{client_name}({name})"

    async def connect(self):
        await self.connection.start()
        await self.dispatcher.dispatch_event(self, ConnectHandler)
        self.user = await self.get_me()

    async def disconnect(self):
        await self.connection.stop()
        await self.dispatcher.dispatch_event(self, DisconnectHandler)

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

    async def execute(self, method: str, service: str, **data):
        data = {k: v for k, v in data.items() if v is not None}
        files = {}
        for key, value in data.copy().items():
            if isinstance(value, (bytes, BufferedReader)):
                files[key] = value
                del data[key]
            elif isinstance(value, dict):
                data[key] = dumps(value)
        while True:
            try:
                return await self.connection.request(method, service, data=data, files=files)
            except TooManyRequestsError as error:
                if error.seconds <= self.sleep_threshold:
                    print(f"[Too many requests] retry after: {error.seconds} (caused by {service})")
                    await sleep(error.seconds)
                else:
                    raise error

    async def initialize(self):
        await self.dispatcher.start()
        await self.dispatcher.dispatch_event(self, InitializeHandler)

    async def shutdown(self):
        await self.dispatcher.dispatch_event(self, ShutdownHandler)
        await self.dispatcher.stop()

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
                        await self.dispatcher.dispatch_event(self, DisconnectHandler)
                except Exception as error:
                    await self.dispatcher.dispatch_event(self, error)
                else:
                    if self.is_disconnected:
                        self.is_disconnected = False
                        await self.dispatcher.dispatch_event(self, ConnectHandler)
                    for update in updates:
                        if last_update_id is not None and last_update_id >= update.id:
                            continue
                        last_update_id = update.id
                        await self.dispatcher.dispatch_event(self, update.get_effective_update())
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
            return
        finally:
            if self.dispatcher.is_started:
                self.shutdown()
            self.disconnect()

    async def download(self, file_id: str):
        return await self.connection.download_file(file_id)

    async def resolve_peer_id(self, chat_id):
        if isinstance(chat_id, str) and not chat_id.isnumeric():
            peer = await self.get_chat(chat_id)
            return peer.id
        return chat_id

    def create_referral_link(self, name: str, value: str) -> str:
        return f"{self.connection.short_url}/{self.user.username}?{name}={value}"
