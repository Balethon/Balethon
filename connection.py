from aiohttp import (
    ClientSession,
    ServerTimeoutError,
    ClientConnectionError
)
    
class Connections:
    
    def __init__(self, token, time_out=20):
        self.token = token
        self.time_out = time_out
        self.session = None
    
    async def connect(self):
        self.session = ClientSession()
        
    async def disconnect(self):
        await self.session.close()
        self.session = None
        
    @property
    def url(self):
        return f"https://tapi.bale.ai/bot{self.token}"
    
    async def execute(self, request_type, method, json=None):
        try:
            async with self.session.request(
                method=request_type,
                url=f"{self.url}/{method}",
                json=json,
                timeout=self.time_out
            ) as response:
                
#                await self.disconnect()
                if not response.ok:
                    return "Not Found Token"
                response = await response.json()
                if response.get("result") is None:
                    return f"Bad Request: \n {response}"
                return response
                
        except ServerTimeoutError:
            return "Time Out"
        except ClientConnectionError:
            return "Connection Error"
 