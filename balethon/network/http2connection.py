from typing import AsyncGenerator
from datetime import datetime
from math import modf

from httpx import AsyncClient
from httpx._types import ProxyTypes

from ..errors import RPCError


class HTTP2Connection:
    TIMEOUT = 300
    BASE_URL = "https://next-ws.bale.ai"
    ORIGIN = "https://web.bale.ai"
    APP_VERSION = "147558"
    BROWSER_TYPE = "1"
    BROWSER_VERSION = "137.0.0.0"
    OS_TYPE = "3"

    def __init__(
            self,
            proxy: ProxyTypes = None,
    ):
        self.client = AsyncClient(
            http2=True,
            proxy=proxy,
            timeout=self.TIMEOUT
        )
        self.session_id = self.get_normalized_timestamp()

    @staticmethod
    def get_normalized_timestamp() -> str:
        timestamp = datetime.now().timestamp()
        frac, whole = modf(timestamp)
        return f"{int(whole)}{int(frac * 1000)}"

    def build_request_headers(self):
        return {
            "content-type": "application/grpc-web+proto",
            "app_version": self.APP_VERSION,
            "browser_type": self.BROWSER_TYPE,
            "browser_version": self.BROWSER_VERSION,
            "os_type": self.OS_TYPE,
            "origin": self.ORIGIN,
            "session_id": self.session_id
        }

    @staticmethod
    def add_grpc_frame(data: bytes) -> bytes:
        header = b"\x00" + len(data).to_bytes(4, "big")
        return header + data

    @staticmethod
    def strip_grpc_frame(data: bytes) -> bytes:
        length = int.from_bytes(data[1:5], "big")
        return data[5:5 + length]

    async def request(self, service: str, content: bytes):
        response = await self.client.post(
            url=f"{self.BASE_URL}/{service}",
            content=self.add_grpc_frame(content),
            headers=self.build_request_headers()
        )
        status = response.headers.get("grpc-status")
        if status is not None and status != 0:
            description = response.headers.get("grpc-message")
            raise RPCError(status, description, reason=service)
        return self.strip_grpc_frame(response.content)

    @staticmethod
    async def generate_chunks(file: bytes, chunk_size: int) -> AsyncGenerator[bytes, None]:
        file_size = len(file)
        for i in range(0, file_size, chunk_size):
            yield file[i : i + chunk_size]

    async def upload_file(self, url: str, file: bytes, chunk_size: int = None) -> bool:
        content = self.generate_chunks(file, chunk_size) if chunk_size else file
        response = await self.client.put(url, content=content)
        return response.is_success

    async def download_file(self, url: str, timeout: int = None):
        response = await self.client.get(url, timeout=timeout)
        response.raise_for_status()
        return response.read()
