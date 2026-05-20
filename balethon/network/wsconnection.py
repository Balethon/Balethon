import asyncio
import ssl
import base64
import hashlib
import struct
from urllib.parse import urlparse
import os
from datetime import datetime
from math import modf
from random import randint
from typing import Optional

try:
    from google.protobuf.message import Message
except ImportError:
    pass

from ..errors import RPCError
try:
    from balethon.proto import requests, ws
except ImportError:
    pass


class WSConnection:
    TIMEOUT = 20
    WEBSOCKET_URI = "wss://next-ws.bale.ai/ws/"
    ORIGIN = "https://web.bale.ai"
    APP_VERSION = 86550
    BROWSER_TYPE = "1"
    BROWSER_VERSION = 3471765337684194354
    OS_TYPE = "3"

    def __init__(
            self,
            access_token: str,
            timeout: int = None,
            websocket_uri: str = None,
            origin: str = None,
            app_version: int = None,
            browser_type: str = None,
            browser_version: int = None,
            os_type: str = None
    ):
        self.access_token = access_token
        self.timeout = timeout or self.TIMEOUT
        self.reader: Optional[asyncio.StreamReader] = None
        self.writer: Optional[asyncio.StreamWriter] = None
        self.websocket_uri = websocket_uri or self.WEBSOCKET_URI
        self.origin = origin or self.ORIGIN
        self.app_version = app_version or self.APP_VERSION
        self.browser_type = browser_type or self.BROWSER_TYPE
        self.browser_version = browser_version or self.BROWSER_VERSION
        self.os_type = os_type or self.OS_TYPE
        self.additional_headers = {"Cookie": f"access_token={access_token}"}
        self.is_started = False
        self.send_queue = asyncio.Queue()
        self.recv_queue = asyncio.Queue()
        self.responses = []
        self.session_id: Optional[str] = None
        self.index = 1
        self._send_task = None
        self._recv_task = None
        self._response_lock = asyncio.Lock()
        self.error = None

    async def websocket_handshake(self, host: str, path: str, port: int):
        key = base64.b64encode(hashlib.sha1().digest()[:16]).decode()

        handshake = (
            f"GET {path} HTTP/1.1\r\n"
            f"Host: {host}:{port}\r\n"
            f"Upgrade: websocket\r\n"
            f"Connection: Upgrade\r\n"
            f"Sec-WebSocket-Key: {key}\r\n"
            f"Sec-WebSocket-Version: 13\r\n"
            f"Origin: {self.origin}\r\n"
        )

        for header, value in self.additional_headers.items():
            handshake += f"{header}: {value}\r\n"

        handshake += "\r\n"

        self.writer.write(handshake.encode())
        await self.writer.drain()

        response = b""
        while b"\r\n\r\n" not in response:
            chunk = await self.reader.read(1024)
            if not chunk:
                raise ConnectionError("Connection closed during handshake")
            response += chunk

        if b"101 Switching Protocols" not in response:
            raise Exception("WebSocket handshake failed")

    async def send_frame(self, data: bytes, opcode: int = 0x2):
        frame = bytearray()
        frame.append(0x80 | opcode)

        payload_len = len(data)
        if payload_len < 126:
            frame.append(0x80 | payload_len)
        elif payload_len < 65536:
            frame.append(0x80 | 126)
            frame.extend(struct.pack(">H", payload_len))
        else:
            frame.append(0x80 | 127)
            frame.extend(struct.pack(">Q", payload_len))

        mask = os.urandom(4)
        frame.extend(mask)

        masked_data = bytearray(data)
        for i in range(len(masked_data)):
            masked_data[i] ^= mask[i % 4]

        frame.extend(masked_data)
        self.writer.write(bytes(frame))
        await self.writer.drain()

    async def recv_frame(self):
        header = await self.reader.readexactly(2)
        if len(header) < 2:
            raise ConnectionError("Connection closed")

        opcode = header[0] & 0x0F
        masked = (header[1] & 0x80) != 0
        payload_len = header[1] & 0x7F

        if payload_len == 126:
            payload_len = struct.unpack(">H", await self.reader.readexactly(2))[0]
        elif payload_len == 127:
            payload_len = struct.unpack(">Q", await self.reader.readexactly(8))[0]

        if masked:
            mask = await self.reader.readexactly(4)

        payload = await self.reader.readexactly(payload_len)

        if masked:
            payload = bytearray(payload)
            for i in range(len(payload)):
                payload[i] ^= mask[i % 4]
            payload = bytes(payload)

        if opcode == 0x8:  # Close
            close_code = None
            close_reason = None

            if payload_len >= 2:
                close_code_bytes = payload[:2]
                close_reason_bytes = payload[2:]

                close_code = struct.unpack(">H", close_code_bytes)[0]

                try:
                    close_reason = close_reason_bytes.decode("utf-8")
                except UnicodeDecodeError:
                    close_reason = None

            if close_code == 4401:
                raise RPCError(close_code, description=close_reason)

            raise ConnectionError("Connection closed by server")

        elif opcode == 0x9:  # Ping
            await self.send_frame(payload, opcode=0xA)  # Pong
            return await self.recv_frame()

        elif opcode == 0xA:  # Pong
            return await self.recv_frame()

        return payload

    @staticmethod
    def create_rid():
        return randint(1000000000000000, 9999999999999999)

    @staticmethod
    def get_normalized_timestamp() -> str:
        timestamp = datetime.now().timestamp()
        frac, whole = modf(timestamp)
        return f"{int(whole)}{int(frac * 1000)}"

    async def keep_alive(self):
        return await self.send(requests.KeepAliveRequest(
            payloads=requests.KeepAlive(value_should_2=2),
        ))

    async def start(self):
        parsed = urlparse(self.websocket_uri)
        host = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == "wss" else 80)
        path = parsed.path or "/"

        if parsed.scheme == "wss":
            ssl_context = ssl.create_default_context()
            self.reader, self.writer = await asyncio.wait_for(
                asyncio.open_connection(host, port, ssl=ssl_context),
                timeout=self.timeout
            )
        else:
            self.reader, self.writer = await asyncio.wait_for(
                asyncio.open_connection(host, port),
                timeout=self.timeout
            )

        await self.websocket_handshake(host, path, port)

        self.session_id = self.get_normalized_timestamp()
        await self.keep_alive()
        self.is_started = True

        # Start background tasks
        self._send_task = asyncio.create_task(self.send_loop())
        self._recv_task = asyncio.create_task(self.recv_loop())

    async def stop(self):
        self.is_started = False

        # Cancel background tasks
        if self._send_task:
            self._send_task.cancel()
            try:
                await self._send_task
            except asyncio.CancelledError:
                pass

        if self._recv_task:
            self._recv_task.cancel()
            try:
                await self._recv_task
            except asyncio.CancelledError:
                pass

        # Close connection
        if self.writer:
            try:
                await self.send_frame(b"", opcode=0x8)
                self.writer.close()
                await self.writer.wait_closed()
            except:
                pass
            self.writer = None
            self.reader = None

    async def send_loop(self):
        while self.is_started:
            try:
                message = await asyncio.wait_for(self.send_queue.get(), timeout=1)
                await self.send_frame(message)
            except asyncio.TimeoutError:
                continue
            except asyncio.CancelledError:
                break
            except Exception:
                if not self.is_started:
                    break
                continue

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
                message = await self.recv_frame()
                if self.is_update(message):
                    await self.recv_queue.put(message)
                if self.is_response(message):
                    async with self._response_lock:
                        self.responses.append(message)
            except (RPCError, ConnectionError) as error:
                self.error = error
                self.is_started = False
                break
            except asyncio.CancelledError:
                break
            except Exception:
                if not self.is_started:
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
        start_time = asyncio.get_event_loop().time()

        while True:
            if self.error is not None:
                raise self.error

            async with self._response_lock:
                for response in self.responses:
                    deserialized_response = self.deserialize_message(response)
                    if deserialized_response.index == index:
                        self.responses.remove(response)
                        result = deserialized_response.response or deserialized_response.error
                        if isinstance(result, ws.Error):
                            raise RPCError(code=result.code, description=result.message, reason=None)
                        return result

            elapsed = asyncio.get_event_loop().time() - start_time
            if elapsed >= self.timeout:
                raise asyncio.TimeoutError(f"Response with index {index} not received within {self.timeout}s")

            await asyncio.sleep(0.1)

    def build_request_metadata(self):
        return requests.Metadata(
            key_values=[
                requests.MetadataKeyValues(
                    key="app_version",
                    value=requests.MetadataValues(
                        string_value=str(self.app_version),
                    )
                ),
                requests.MetadataKeyValues(
                    key="browser_type",
                    value=requests.MetadataValues(
                        string_value=str(self.browser_type),
                    )
                ),
                requests.MetadataKeyValues(
                    key="browser_version",
                    value=requests.MetadataValues(
                        msg_value=requests.MetadataComplexValues(
                            fixed64_value=self.browser_version,
                        ),
                    )
                ),
                requests.MetadataKeyValues(
                    key="os_type",
                    value=requests.MetadataValues(
                        string_value=self.os_type,
                    )
                ),
                requests.MetadataKeyValues(
                    key="session_id",
                    value=requests.MetadataValues(
                        string_value=self.session_id,
                    )
                ),
            ]
        )

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
        response = await self.wait_for_response(request_index)
        return response
