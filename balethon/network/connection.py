from json import loads

from httpx import AsyncClient
from bs4 import BeautifulSoup

from ..errors import RPCError


class Connection:
    TIMEOUT = 20
    BASE_URL = "https://tapi.bale.ai"
    SHORT_URL = "https://ble.ir"

    def __init__(self, token, time_out=None, base_url=None):
        self.token = token
        self.client = None
        self.is_started = False
        self.time_out = time_out or self.TIMEOUT
        self.base_url = base_url or self.BASE_URL

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client = AsyncClient()

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        await self.client.aclose()
        self.client = None

    def bot_url(self):
        return f"{self.base_url}/bot{self.token}"

    def file_url(self, file_id):
        return f"{self.base_url}/file/bot{self.token}/{file_id}"

    async def get_info_by_username(self, username):
        response = await self.client.get(f"{self.SHORT_URL}/{username}")
        soup = BeautifulSoup(response.text, "html.parser")
        json_info = soup.html.body.script.contents[0]
        return loads(json_info)

    async def request(self, method, service, data=None, files=None, json=None):
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

    async def download_file(self, file_id):
        response = await self.client.get(self.file_url(file_id))
        if response.status_code != 200:
            response_json = response.json()
            raise RPCError.create(response.status_code, response_json.get("description"), "downloadFile")
        return response.read()
