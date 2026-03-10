from datetime import datetime
from math import modf

from httpx import AsyncClient
from httpx._types import ProxyTypes


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

    async def request(self, method: str, service: str, content: bytes):
        response = await self.client.request(
            method,
            url=f"{self.BASE_URL}/{service}",
            content=self.add_grpc_frame(content),
            headers=self.build_request_headers()
        )
        return self.strip_grpc_frame(response.content)

    async def upload_file(self, url: str, file: bytes) -> bool:
        response = await self.client.put(url, content=file)
        return response.is_success
