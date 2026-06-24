from json import dumps, loads
from asyncio import get_event_loop, sleep
from inspect import iscoroutine, iscoroutinefunction, stack
from io import BufferedReader, BytesIO
from typing import get_type_hints
import re
from pathlib import Path
import sys
from typing import Union
import base64

from httpx import ConnectError
try:
    from google.protobuf.message import Message as ProtobufMessage
except ImportError:
    protobuf_installed = False
else:
    protobuf_installed = True

from .messages import Messages
from .updates import Updates
from .users import Users
from .attachments import Attachments
from .chats import Chats
from .invite_links import InviteLinks
from .payments import Payments
from .stickers import Stickers
from .auth import Auth
from ..objects import Object, wrap, unwrap, Chat, User, Message
from ..errors import TooManyRequestsError, RPCError
from ..network import HTTPConnection, WSConnection, HTTP2Connection
from ..dispatcher import Dispatcher, Chain, PrintingChain
from ..event_handlers import ConnectHandler, DisconnectHandler, InitializeHandler, ShutdownHandler
from ..smart_call import remove_unwanted_keyword_parameters
from ..sync_support import add_sync_support_to_object
try:
    from ..proto import responses
except ImportError:
    pass


@add_sync_support_to_object
class Client(Chain, Messages, Updates, Users, Attachments, Chats, InviteLinks, Payments, Stickers, Auth):
    WORKDIR = Path(sys.argv[0]).parent

    def __init__(
            self,
            token_or_phone_number: str,
            async_workers: int = None,
            sync_workers: int = None,
            use_concurrency: bool = True,
            time_out: int = None,
            workdir: Union[Path, str] = None,
            sleep_threshold: int = 60,
            proxy=None,
            base_url: str = None,
            short_url: str = None
    ):
        super().__init__("default", None, PrintingChain())
        self.token_or_phone_number = token_or_phone_number
        self.time_out = time_out
        if workdir is None:
            self.workdir = self.WORKDIR
        else:
            self.workdir = workdir if isinstance(workdir, Path) else Path(workdir)
        self.dispatcher = Dispatcher(
            self,
            async_workers=async_workers,
            sync_workers=sync_workers,
            use_concurrency=use_concurrency
        )
        if re.match(r"^(\d+):(.+)$", token_or_phone_number):
            self.ws_connection = None
            self.http2_connection = None
            self.http_connection = HTTPConnection(token_or_phone_number, time_out, proxy, base_url, short_url)
        else:
            if not protobuf_installed:
                raise ImportError(
                    "Using Balethon userbots but the required dependencies are not installed\n"
                    "Make sure to install balethon using `pip install Balethon[userbots]`"
                )
            jwt = self.load_session()
            self.ws_connection = None if jwt is None else WSConnection(jwt, time_out)
            self.http2_connection = HTTP2Connection() if jwt is None else HTTP2Connection(jwt)
            self.http_connection = None
        self.sleep_threshold = sleep_threshold
        self.user = None
        self.is_disconnected = False
        self.last_update_id = None

    def is_userbot(self):
        return self.http_connection is None

    def __repr__(self):
        client_name = type(self).__name__
        try:
            name = self.user.full_name
        except AttributeError:
            name = "Not initialized yet"
        return f"{client_name}({name})"

    async def connect(self):
        if self.is_userbot():
            await self.http2_connection.start()
            if self.ws_connection is None:
                await self.auth()
            await self.ws_connection.start()
        else:
            await self.http_connection.start()
        self.user = await self.get_me()

    async def disconnect(self):
        if self.is_userbot():
            await self.http2_connection.stop()
            await self.ws_connection.stop()
        else:
            await self.http_connection.stop()

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

    async def execute_http(self, service: str, json: bool = None, **data):
        data = {k: v for k, v in data.items() if v is not None}
        files = {}
        if json is None:
            for value in data.values():
                if isinstance(value, (bytes, BufferedReader, BytesIO)):
                    json = False
                    break
            else:
                json = True
        for key, value in data.items():
            data[key] = unwrap(value)
        if not json:
            for key, value in data.copy().items():
                if isinstance(value, (bytes, BufferedReader, BytesIO)):
                    files[key] = value
                    del data[key]
                elif isinstance(value, dict):
                    data[key] = dumps(value)
        while True:
            try:
                if json:
                    return await self.http_connection.request(service, json=data)
                return await self.http_connection.request(service, data=data, files=files)
            except TooManyRequestsError as error:
                if error.seconds <= self.sleep_threshold:
                    print(f"[Too many requests] retry after: {error.seconds} (caused by {service})")
                    await sleep(error.seconds)
                else:
                    raise error

    async def execute(self, service: Union[str, "ProtobufMessage"], json: bool = None, **data):
        if not self.is_userbot():
            return await self.execute_http(service, json=json, **data)
        if service.http2:
            return await self.execute_http2(service)
        return await self.execute_ws(service)

    async def auto_execute(self, service: str, data: dict, json: bool = None):
        bound_method_name = stack()[1].function
        bound_method = getattr(self, bound_method_name)
        type_hints = get_type_hints(bound_method)
        del data["self"]
        del type_hints["self"]
        return_type_hint = type_hints.pop("return")
        result = await self.execute(service, json, **data)
        result = wrap(return_type_hint, result)
        if isinstance(result, Object):
            result.bind(self)
        return result

    async def execute_ws(self, payload: "ProtobufMessage"):
        response = await self.ws_connection.request(payload.service_name, payload.method, payload)
        payload_class_name = type(payload).__name__
        response_class = getattr(responses, payload_class_name, None)
        if response_class is None:
            return response
        result = response_class()
        result.ParseFromString(response)
        return result

    async def execute_http2(self, payload: "ProtobufMessage"):
        response = await self.http2_connection.request(f"{payload.service_name}/{payload.method}", payload)
        payload_class_name = type(payload).__name__
        response_class = getattr(responses, payload_class_name, None)
        if response_class is None:
            return response
        result = response_class()
        result.ParseFromString(response)
        return result

    async def initialize(self):
        await self.dispatcher.start()
        await self.dispatcher.dispatch_event(self, InitializeHandler)

    async def shutdown(self):
        await self.dispatcher.dispatch_event(self, ShutdownHandler)
        await self.dispatcher.stop()

    def save_session(self, jwt):
        with open(self.workdir / f"{self.token_or_phone_number}.session", "w", encoding="utf-8") as f:
            f.write(jwt)

    def load_session(self):
        try:
            with open(self.workdir / f"{self.token_or_phone_number}.session", encoding="utf-8") as f:
                return f.read()
        except FileNotFoundError:
            return None

    @staticmethod
    def decode_jwt(jwt: str) -> dict:
        header, payload, signature = jwt.split(".", maxsplit=2)

        def decode_part(part: str) -> dict:
            padded = part + "=" * (4 - len(part) % 4)
            decoded = base64.urlsafe_b64decode(padded)
            return loads(decoded)

        return {
            "header": decode_part(header),
            "payload": decode_part(payload),
            "signature": signature
        }

    async def start_polling(self, clear_pending_updates: bool = True):
        await self.delete_webhook()
        await self.initialize()
        while True:
            try:
                if self.last_update_id is None:
                    try:
                        if not clear_pending_updates:
                            raise Exception()
                        updates = await self.get_updates(offset=-1)
                    except Exception:
                        updates = await self.get_updates()
                else:
                    updates = await self.get_updates(offset=self.last_update_id + 1)
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
                    if self.last_update_id is not None and self.last_update_id >= update.id:
                        continue
                    self.last_update_id = update.id
                    await self.dispatcher.dispatch_event(self, update.get_effective_update())

    async def auth(self):
        sent_code = await self.start_phone_auth(self.token_or_phone_number)
        while True:
            try:
                auth = await self.validate_code(sent_code.transaction_hash, input("Enter phone code: "))
            except RPCError as error:
                if error.description == "PHONE_NUMBER_UNOCCUPIED":
                    auth = await self.sign_up(sent_code.transaction_hash, input("Enter a name for your account: "))
                    break
                elif error.description == "PHONE_CODE_INVALID":
                    print("The phone code is invalid, try again")
                elif error.description == "":  # TODO: Add description for password requirement error
                    auth = await self.validate_password(sent_code.transaction_hash, input("Enter your password: "))
                    break
                else:
                    raise error
            else:
                break
        self.save_session(auth.jwt.value)
        self.http2_connection.access_token = auth.jwt.value
        self.ws_connection = WSConnection(auth.jwt.value, self.time_out)

    async def start_websocket(self):
        await self.initialize()
        while True:
            try:
                raw_update = await self.ws_connection.recv()
                if raw_update.update and raw_update.update.composed_update and raw_update.update.composed_update.message:
                    raw_message = raw_update.update.composed_update.message
                    if raw_message.rid == 0:
                        continue
                    message = Message.from_protobuf(raw_message)
                    message.bind(self)
                    await self.dispatcher.dispatch_event(self, message)
            except Exception as error:
                await self.dispatcher.dispatch_event(self, error)

    def run(self, function=None, **kwargs):
        try:
            self.connect()
            if function is None:
                if self.is_userbot():
                    self.start_websocket()
                else:
                    self.start_polling(**kwargs)
            elif iscoroutine(function):
                loop = get_event_loop()
                loop.run_until_complete(function)
            elif iscoroutinefunction(function):
                kwargs = remove_unwanted_keyword_parameters(function, client=self, **kwargs)
                loop = get_event_loop()
                loop.run_until_complete(function(**kwargs))
            else:
                kwargs = remove_unwanted_keyword_parameters(function, client=self, **kwargs)
                function(**kwargs)
        except KeyboardInterrupt:
            return
        finally:
            if self.dispatcher.is_started:
                self.shutdown()
            self.disconnect()

    async def download(self, file_id: str):
        if self.is_userbot():
            file = await self.get_file(file_id)
            file_url_description = file.file_url
            return await self.http2_connection.download_file(file_url_description.url, file_url_description.timeout)
        return await self.http_connection.download_file(file_id)

    async def resolve_peer_id(self, chat_id):
        if isinstance(chat_id, str) and not chat_id.isnumeric():
            peer = await self.get_chat(chat_id)
            return peer.id
        if isinstance(chat_id, (Chat, User)):
            return chat_id.id
        return chat_id

    def create_referral_link(self, name, value) -> str:
        return f"{self.http_connection.short_url}/{self.user.username}?{name}={value}"
