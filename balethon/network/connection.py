from aiohttp import ClientSession

from ..errors import RPCError


class Connection:

    def __init__(self, token, time_out):
        self.token = token
        self.time_out = time_out
        self.client_session = None
        self.is_started = False
        self.base_url = "https://tapi.bale.ai/bot"

    async def start(self):
        if self.is_started:
            raise ConnectionError("Client is already connected")
        self.is_started = True
        self.client_session = ClientSession()

    async def stop(self):
        if not self.is_started:
            raise ConnectionError("Client is already disconnected")
        self.is_started = False
        await self.client_session.close()
        self.client_session = None

    @property
    def url(self):
        return f"{self.base_url}{self.token}"

    async def execute(self, request_type, method, json=None):
        async with self.client_session.request(
            method=request_type,
            url=f"{self.url}/{method}",
            json=json,
            timeout=self.time_out
        ) as response:
            response = await response.json()
            if not response["ok"]:
                raise RPCError.create(response.get("error_code"), response.get("description"), method)
            return response["result"]
