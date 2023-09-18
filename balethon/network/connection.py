from aiohttp import ClientSession

from ..errors import RPCError


class Connection:

    def __init__(self, token, time_out):
        self.client_session = None
        self.base_url = "https://tapi.bale.ai/bot"
        self.token = token
        self.time_out = time_out
        self.is_started = False

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

    @property
    def url(self):
        return f"{self.base_url}{self.token}"

    async def execute(self, method, service, json=None):
        async with self.client_session.request(
                method,
                f"{self.url}/{service}",
                json=json,
                timeout=self.time_out
        ) as response:
            response_json = await response.json()
            if not response.ok:
                raise RPCError.create(response_json.get("error_code"), response_json.get("description"), service)
            return response_json.get("result")
