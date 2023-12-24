from json import loads
from re import search

from httpx import AsyncClient

from ..errors import RPCError


class Connection:
    TIMEOUT = 20
    BASE_URL = "https://tapi.bale.ai"
    SHORT_URL = "https://ble.ir"

    def __init__(self, token: str, time_out: int = None, proxies=None, base_url: str = None, short_url: str = None):
        self.token: str = token
        self.client: AsyncClient = None
        self.is_started: bool = False
        self.time_out: int = time_out or self.TIMEOUT
        self.proxies = proxies
        self.base_url: str = base_url or self.BASE_URL
        self.short_url: str = short_url or self.SHORT_URL

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client = AsyncClient(proxies=self.proxies)

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        await self.client.aclose()
        self.client = None

    def bot_url(self) -> str:
        return f"{self.base_url}/bot{self.token}"

    def file_url(self, file_id: str) -> str:
        return f"{self.base_url}/file/bot{self.token}/{file_id}"

    async def get_info_by_username(self, username: str) -> str:
        response = await self.client.get(f"{self.short_url}/{username}")
        json_info = search(r"({.*})", response.text)[0]
        return loads(json_info)

    async def request(self, method: str, service: str, data: dict = None, files: dict = None, json: dict = None):
        response = await self.client.request(
                method,
                f"{self.bot_url()}/{service}",
                data=data,
                files=files,
                json=json,
                timeout=self.time_out
        )
        response_json = response.json()
        if response.status_code != 200:
            code = response.status_code or response_json.get("error_code")
            raise RPCError.create(code, response_json.get("description"), service)
        return response_json.get("result")

    async def download_file(self, file_id: str):
        response = await self.client.get(self.file_url(file_id))
        if response.status_code != 200:
            response_json = response.json()
            raise RPCError.create(response.status_code, response_json.get("description"), "downloadFile")
        return response.read()
