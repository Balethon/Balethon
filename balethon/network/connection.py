from aiohttp import (
    ClientSession,
    ServerTimeoutError,
    ClientConnectionError
)


class Connection:

    def __init__(self, token, time_out):
        self.token = token
        self.time_out = time_out
        self.client_session = None

    async def start(self):
        self.client_session = ClientSession()

    async def stop(self):
        await self.client_session.close()
        self.client_session = None

    @property
    def url(self):
        return f"https://tapi.bale.ai/bot{self.token}"

    async def execute(self, request_type, method, json=None):
        try:
            async with self.client_session.request(
                method=request_type,
                url=f"{self.url}/{method}",
                json=json,
                timeout=self.time_out
            ) as response:

                response = await response.json()
                if not response["ok"]:
                    raise Exception(str(response))
                return response["result"]

        except ServerTimeoutError:
            raise Exception("time out")
        except ClientConnectionError:
            raise Exception("Connection Error")
