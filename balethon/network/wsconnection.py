import socket
import ssl
import base64
import hashlib
import struct
from threading import Thread
from queue import Queue
from urllib.parse import urlparse
import os
from datetime import datetime
from math import modf
from random import randint
from typing import Optional

from google.protobuf.message import Message

from balethon.proto import request_pb2
from balethon.proto import response_pb2


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
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(self.timeout)
        self.websocket_uri = websocket_uri or self.WEBSOCKET_URI
        self.origin = origin or self.ORIGIN
        self.app_version = app_version or self.APP_VERSION
        self.browser_type = browser_type or self.BROWSER_TYPE
        self.browser_version = browser_version or self.BROWSER_VERSION
        self.os_type = os_type or self.OS_TYPE
        self.additional_headers = {"Cookie": f"access_token={access_token}"}
        self.is_started = False
        self.send_queue = Queue()
        self.recv_queue = Queue()
        self.responses = []
        self.session_id: Optional[str] = None
        self.index = 1

    def websocket_handshake(self, host: str, path: str, port: int):
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

        self.sock.sendall(handshake.encode())

        response = b""
        while b"\r\n\r\n" not in response:
            response += self.sock.recv(1024)

        if b"101 Switching Protocols" not in response:
            raise Exception("WebSocket handshake failed")

    def send_frame(self, data: bytes, opcode: int = 0x2):
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
        self.sock.sendall(bytes(frame))

    def recv_frame(self):
        header = self.sock.recv(2)
        if len(header) < 2:
            raise ConnectionError("Connection closed")

        opcode = header[0] & 0x0F
        masked = (header[1] & 0x80) != 0
        payload_len = header[1] & 0x7F

        if payload_len == 126:
            payload_len = struct.unpack(">H", self.sock.recv(2))[0]
        elif payload_len == 127:
            payload_len = struct.unpack(">Q", self.sock.recv(8))[0]

        if masked:
            mask = self.sock.recv(4)

        payload = bytearray()
        while len(payload) < payload_len:
            chunk = self.sock.recv(payload_len - len(payload))
            if not chunk:
                raise ConnectionError("Connection closed")
            payload.extend(chunk)

        if masked:
            for i in range(len(payload)):
                payload[i] ^= mask[i % 4]

        if opcode == 0x8:  # Close
            raise ConnectionError("Connection closed by server")
        elif opcode == 0x9:  # Ping
            self.send_frame(bytes(payload), opcode=0xA)  # Pong
            return self.recv_frame()
        elif opcode == 0xA:  # Pong
            return self.recv_frame()

        return bytes(payload)

    @staticmethod
    def create_rid():
        return randint(1000000000000000, 9999999999999999)

    @staticmethod
    def get_normalized_timestamp() -> str:
        timestamp = datetime.now().timestamp()
        frac, whole = modf(timestamp)
        return f"{int(whole)}{int(frac * 1000)}"

    def keep_alive(self):
        return self.send(request_pb2.KeepAliveRequest(
            payloads=request_pb2.KeepAlive(value_should_2=2),
        ))

    def start(self):
        parsed = urlparse(self.websocket_uri)
        host = parsed.hostname
        port = parsed.port or (443 if parsed.scheme == "wss" else 80)
        path = parsed.path or "/"

        if parsed.scheme == "wss":
            context = ssl.create_default_context()
            self.sock = context.wrap_socket(self.sock, server_hostname=host)

        self.sock.connect((host, port))
        self.websocket_handshake(host, path, port)

        self.session_id = self.get_normalized_timestamp()
        self.keep_alive()
        self.is_started = True
        Thread(target=self.send_loop, daemon=True).start()
        Thread(target=self.recv_loop, daemon=True).start()

    def stop(self):
        self.is_started = False
        if self.sock:
            try:
                self.send_frame(b"", opcode=0x8)
                self.sock.close()
            except:
                pass
            self.sock = None

    def send_loop(self):
        while self.is_started:
            try:
                message = self.send_queue.get(timeout=1)
                self.send_frame(message)
            except:
                if not self.is_started:
                    break
                continue

    @classmethod
    def is_update(cls, message):
        deserialized_message = cls.deserialize_message(message)
        return isinstance(deserialized_message, response_pb2.WsUpdate)

    @classmethod
    def is_response(cls, message):
        deserialized_message = cls.deserialize_message(message)
        return isinstance(deserialized_message, response_pb2.WsResponse)

    def recv_loop(self):
        while self.is_started:
            try:
                message = self.recv_frame()
                if self.is_update(message):
                    self.recv_queue.put(message)
                if self.is_response(message):
                    self.responses.append(message)
            except:
                if not self.is_started:
                    break
                continue

    @staticmethod
    def serialize_message(message):
        if isinstance(message, Message):
            message = message.SerializeToString()
        return message

    @staticmethod
    def deserialize_message(message):
        if isinstance(message, bytes):
            response = response_pb2.Response()
            response.ParseFromString(message)
            if str(response.ws_update):
                message = response.ws_update
            elif str(response.ws_response):
                message = response.ws_response
        return message

    def send(self, message):
        message = self.serialize_message(message)
        self.send_queue.put(message)
        return message

    def recv(self):
        message = self.recv_queue.get()
        return self.deserialize_message(message)

    def wait_for_response(self, index: int):
        while True:
            for response in self.responses:
                deserialized_response = self.deserialize_message(response)
                if deserialized_response.index == index:
                    return deserialized_response.response

    def build_request_metadata(self):
        return request_pb2.Metadata(
            key_values=[
                request_pb2.MetadataKeyValues(
                    key="app_version",
                    value=request_pb2.MetadataValues(
                        string_value=str(self.app_version),
                    )
                ),
                request_pb2.MetadataKeyValues(
                    key="browser_type",
                    value=request_pb2.MetadataValues(
                        string_value=str(self.browser_type),
                    )
                ),
                request_pb2.MetadataKeyValues(
                    key="browser_version",
                    value=request_pb2.MetadataValues(
                        msg_value=request_pb2.MetadataComplexValues(
                            fixed64_value=self.browser_version,
                        ),
                    )
                ),
                request_pb2.MetadataKeyValues(
                    key="os_type",
                    value=request_pb2.MetadataValues(
                        string_value=self.os_type,
                    )
                ),
                request_pb2.MetadataKeyValues(
                    key="session_id",
                    value=request_pb2.MetadataValues(
                        string_value=self.session_id,
                    )
                ),
            ]
        )

    def build_request(self, service_name: str, method: str, payload: Message):
        request = request_pb2.Request(
            ws_request=request_pb2.WsRequest(
                service_name=service_name,
                method=method,
                payload=payload.SerializeToString(),
                metadata=self.build_request_metadata(),
                index=self.index
            )
        )
        return request

    def request(self, service_name: str, method: str, payload: Message, wait_for_response=True):
        request = self.build_request(service_name, method, payload)
        request_index = self.index
        self.index += 1
        message = self.send(request)
        if not wait_for_response:
            return message
        return self.wait_for_response(request_index)
