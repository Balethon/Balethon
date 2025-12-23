from httpx import AsyncClient
from httpx._types import ProxyTypes


class HTTP2Conection:
    TIMEOUT = 300

    def __init__(
            self,
            proxy: ProxyTypes = None,
    ):
        self.client = AsyncClient(
            http2=True,
            proxy=proxy,
            timeout=self.TIMEOUT
        )

    async def upload_file(self, url: str, file: bytes) -> bool:
        response = await self.client.put(url, content=file)
        return response.is_success
