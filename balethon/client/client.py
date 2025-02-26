from json import dumps
from asyncio import get_event_loop, sleep
from inspect import iscoroutine, iscoroutinefunction, stack
from io import BufferedReader, BytesIO
from typing import get_type_hints

from httpx import ConnectError

from .messages import Messages
from .updates import Updates
from .users import Users
from .attachments import Attachments
from .chats import Chats
from .invite_links import InviteLinks
from .payments import Payments
from .stickers import Stickers
from ..objects import Object, wrap, unwrap
from ..errors import TooManyRequestsError
from ..network import Connection
from ..dispatcher import Dispatcher, Chain, PrintingChain
from ..event_handlers import ConnectHandler, DisconnectHandler, InitializeHandler, ShutdownHandler
from ..smart_call import remove_unwanted_keyword_parameters
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class Client(Chain, Messages, Updates, Users, Attachments, Chats, InviteLinks, Payments, Stickers):

    def __init__(
            self,
            token: str,
            async_workers: int = None,
            sync_workers: int = None,
            time_out: int = None,
            sleep_threshold: int = 60,
            proxy=None,
            base_url: str = None,
            short_url: str = None
    ):
        super().__init__("default", None, PrintingChain())
        self.dispatcher = Dispatcher(self, async_workers=async_workers, sync_workers=sync_workers)
        self.connection = Connection(token, time_out, proxy, base_url, short_url)
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
        self.user = await self.get_me()

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

    def __enter__(self):
        self.connect()
        return self

    def __exit__(self, *args):
        try:
            self.disconnect()
        except ConnectionError:
            return

    async def execute(self, method: str, service: str, json: bool = None, **data):
        data = {k: v for k, v in data.items() if v is not None}
        files = {}
        if json is None:
            for value in data.values():
                if isinstance(value, (bytes, BufferedReader, BytesIO)):
                    json = False
                    break
            else:
                json = True
        if not json:
            for key, value in data.copy().items():
                if isinstance(value, (bytes, BufferedReader, BytesIO)):
                    files[key] = value
                    del data[key]
                elif isinstance(value, dict):
                    data[key] = dumps(value)
        for key, value in data.items():
            data[key] = unwrap(value)
        while True:
            try:
                if json:
                    return await self.connection.request(method, service, json=data)
                return await self.connection.request(method, service, data=data, files=files)
            except TooManyRequestsError as error:
                if error.seconds <= self.sleep_threshold:
                    print(f"[Too many requests] retry after: {error.seconds} (caused by {service})")
                    await sleep(error.seconds)
                else:
                    raise error

    async def auto_execute(self, method: str, service: str, data: dict, json: bool = None):
        bound_method_name = stack()[1].function
        bound_method = getattr(self, bound_method_name)
        type_hints = get_type_hints(bound_method)
        del data["self"]
        del type_hints["self"]
        return_type_hint = type_hints.pop("return")
        result = await self.execute(method, service, json, **data)
        result = wrap(return_type_hint, result)
        if isinstance(result, Object):
            result.bind(self)
        return result

    async def initialize(self):
        await self.dispatcher.start()
        await self.dispatcher.dispatch_event(self, InitializeHandler)

    async def shutdown(self):
        await self.dispatcher.dispatch_event(self, ShutdownHandler)
        await self.dispatcher.stop()

    async def start_polling(self):
        await self.delete_webhook()
        await self.initialize()
        last_update_id = None
        while True:
            try:
                if last_update_id is None:
                    updates = await self.get_updates()
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

    def create_referral_link(self, name, value) -> str:
        return f"{self.connection.short_url}/{self.user.username}?{name}={value}"
