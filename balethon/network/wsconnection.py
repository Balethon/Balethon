import asyncio
from datetime import datetime
from math import modf
from random import randint
from typing import Optional

try:
    from google.protobuf.message import Message
except ImportError:
    pass
try:
    from websockets.asyncio.client import ClientConnection, connect
    from websockets import (
        ConnectionClosedOK,
        ConnectionClosedError
    )
except ImportError:
    pass

from ..errors import RPCError
try:
    from balethon.proto import structs, ws
except ImportError:
    pass


class WSConnection:
    TIMEOUT = 20
    WEBSOCKET_URI = "wss://next-ws.bale.ai/ws/"
    ORIGIN = "https://web.bale.ai"
    APP_VERSION = "86550"
    BROWSER_TYPE = "1"
    BROWSER_VERSION = "137.0.0.0"
    OS_TYPE = "3"

    def __init__(
            self,
            access_token: str,
            timeout: int = None,
            websocket_uri: str = None,
            origin: str = None,
            app_version: str = None,
            browser_type: str = None,
            browser_version: int = None,
            os_type: str = None
    ):
        self.access_token = access_token
        self.timeout = timeout or self.TIMEOUT
        self.websocket_uri = websocket_uri or self.WEBSOCKET_URI
        self.origin = origin or self.ORIGIN
        self.app_version = app_version or self.APP_VERSION
        self.browser_type = browser_type or self.BROWSER_TYPE
        self.browser_version = browser_version or self.BROWSER_VERSION
        self.os_type = os_type or self.OS_TYPE
        self.ws: Optional[ClientConnection] = None
        self.is_started = False
        self.send_queue = asyncio.Queue()
        self.recv_queue = asyncio.Queue()
        self.pending: dict[int, asyncio.Future] = {}
        self.pending_lock = asyncio.Lock()
        self.session_id: Optional[str] = None
        self.index = 1
        self.send_task = None
        self.recv_task = None
        self.error = None

    @staticmethod
    def create_rid():
        return randint(1000000000000000, 9999999999999999)

    @staticmethod
    def get_normalized_timestamp() -> str:
        timestamp = datetime.now().timestamp()
        frac, whole = modf(timestamp)
        return f"{int(whole)}{int(frac * 1000)}"

    async def keep_alive(self):
        return await self.send(ws.ClientPack(ping=ws.Ping(id=2)))

    async def start(self):
        extra_headers = {
            "Cookie": f"access_token={self.access_token}",
            "Origin": self.origin
        }

        self.ws = await asyncio.wait_for(
            connect(
                self.websocket_uri,
                additional_headers=extra_headers,
                open_timeout=self.timeout,
                close_timeout=self.timeout,
                ping_interval=20,
                ping_timeout=self.timeout
            ),
            timeout=self.timeout
        )

        self.session_id = self.get_normalized_timestamp()
        await self.keep_alive()
        self.is_started = True

        self.send_task = asyncio.create_task(self.send_loop())
        self.recv_task = asyncio.create_task(self.recv_loop())

    async def stop(self):
        self.is_started = False

        for task in (self.send_task, self.recv_task):
            if task:
                task.cancel()
                try:
                    await task
                except asyncio.CancelledError:
                    pass

        if self.ws:
            try:
                await asyncio.wait_for(self.ws.close(), timeout=self.timeout)
            except Exception:
                pass
            self.ws = None

    async def send_loop(self):
        while self.is_started:
            try:
                message = await asyncio.wait_for(self.send_queue.get(), timeout=1)
                await self.ws.send(message)
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                break
            except ConnectionClosedOK:
                self.is_started = False
                break
            except ConnectionClosedError as error:
                code = error.rcvd.code if error.rcvd else None
                reason = error.rcvd.reason if error.rcvd else None
                if code == 4401:
                    self.error = RPCError(code, description=reason)
                else:
                    self.error = ConnectionError(f"Connection closed by server (code={code}, reason={reason})")
                self.is_started = False
                break
            except Exception as error:
                if not self.is_started:
                    break
                self.error = error
                self.is_started = False
                break

    @classmethod
    def is_update(cls, message):
        deserialized_message = cls.deserialize_message(message)
        return isinstance(deserialized_message, ws.Update)

    @classmethod
    def is_response(cls, message):
        deserialized_message = cls.deserialize_message(message)
        return isinstance(deserialized_message, ws.Response)

    async def recv_loop(self):
        while self.is_started:
            try:
                raw = await self.ws.recv()
                if self.is_update(raw):
                    await self.recv_queue.put(raw)
                if self.is_response(raw):
                    response = self.deserialize_message(raw)
                    async with self.pending_lock:
                        future = self.pending.pop(response.index, None)
                    if future and not future.done():
                        future.set_result(raw)
            except ConnectionClosedOK:
                self.is_started = False
                break
            except ConnectionClosedError as error:
                code = error.rcvd.code if error.rcvd else None
                reason = error.rcvd.reason if error.rcvd else None
                if code == 4401:
                    self.error = RPCError(code, description=reason)
                else:
                    self.error = ConnectionError(f"Connection closed by server (code={code}, reason={reason})")
                self.is_started = False
                break
            except asyncio.CancelledError:
                break
            except Exception as error:
                if not self.is_started:
                    break
                self.error = error
                self.is_started = False
                break

    @staticmethod
    def serialize_message(message):
        if isinstance(message, Message):
            message = message.SerializeToString()
        return message

    @staticmethod
    def deserialize_message(message):
        if isinstance(message, bytes):
            response = ws.ServerPack()
            response.ParseFromString(message)
            if str(response.update):
                message = response.update
            elif str(response.response):
                message = response.response
        return message

    async def send(self, message):
        message = self.serialize_message(message)
        await self.send_queue.put(message)
        return message

    async def recv(self):
        message = await self.recv_queue.get()
        return self.deserialize_message(message)

    async def wait_for_response(self, index: int):
        if self.error is not None:
            raise self.error

        future = asyncio.get_running_loop().create_future()
        async with self.pending_lock:
            self.pending[index] = future

        try:
            raw = await asyncio.wait_for(future, timeout=self.timeout)

        except asyncio.TimeoutError:
            async with self.pending_lock:
                self.pending.pop(index, None)
            raise

        response = self.deserialize_message(raw)
        return response.error if response.HasField("error") else response.response

    def build_request_metadata(self):
        return structs.MapValue(items=[
            structs.MapValueItem(
                key="app_version",
                value=structs.RawValue(string_value=self.app_version)
            ),
            structs.MapValueItem(
                key="browser_type",
                value=structs.RawValue(string_value=self.browser_type)
            ),
            structs.MapValueItem(
                key="browser_version",
                value=structs.RawValue(string_value=self.browser_version)
            ),
            structs.MapValueItem(
                key="os_type",
                value=structs.RawValue(string_value=self.os_type)
            ),
            structs.MapValueItem(
                key="session_id",
                value=structs.RawValue(string_value=self.session_id)
            ),
        ])

    def build_request(self, service_name: str, method: str, payload: "Message"):
        request = ws.ClientPack(
            ws_request=ws.Request(
                service_name=service_name,
                method=method,
                payload=payload.SerializeToString(),
                metadata=self.build_request_metadata(),
                index=self.index
            )
        )
        return request

    async def request(self, service_name: str, method: str, payload: "Message", wait_for_response: bool = True):
        request = self.build_request(service_name, method, payload)
        request_index = self.index
        self.index += 1
        message = await self.send(request)
        if not wait_for_response:
            return message
        result = await self.wait_for_response(request_index)
        if isinstance(result, ws.Error):
            raise RPCError(code=result.code, description=result.message, reason=f"{service_name}/{method}")
        return result
