from json import dumps

from aiohttp import ClientSession, FormData

from ..errors import RPCError


class Connection:
    TIMEOUT = 20
    BASE_URL = "https://tapi.bale.ai"

    def __init__(self, token, time_out=None, base_url=None):
        self.token = token
        self.client_session = None
        self.is_started = False
        self.time_out = time_out or self.TIMEOUT
        self.base_url = base_url or self.BASE_URL

    async def start(self):
        if self.is_started:
            raise ConnectionError("Connection is already started")
        self.is_started = True
        self.client_session = ClientSession()

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Connection is already stopped")
        self.is_started = False
        await self.client_session.close()
        self.client_session = None

    def bot_url(self):
        return f"{self.base_url}/bot{self.token}"

    def file_url(self, file_id):
        return f"{self.base_url}/file/bot{self.token}/{file_id}"

    async def request(self, method, service, data=None):
        if data is not None:
            data = {k: v for k, v in data.items() if v is not None}
            form_data = FormData()
            for key, value in data.items():
                if isinstance(value, bytes):
                    form_data.add_field(key, value)
                elif isinstance(value, str):
                    form_data.add_field(key, value, content_type="application/json")
                else:
                    form_data.add_field(key, dumps(value), content_type="application/json")
        else:
            form_data = None
        async with self.client_session.request(
                method,
                f"{self.bot_url()}/{service}",
                data=form_data,
                timeout=self.time_out
        ) as response:
            response_json = await response.json()
            if not response.ok:
                code = response.status or response_json.get("error_code")
                raise RPCError.create(code, response_json.get("description"), service)
            return response_json.get("result")

    async def download_file(self, file_id):
        async with self.client_session.get(self.file_url(file_id)) as response:
            if not response.ok:
                response_json = await response.json()
                raise RPCError.create(response.status, response_json.get("description"), "downloadFile")
            return await response.read()
