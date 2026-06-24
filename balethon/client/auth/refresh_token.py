import balethon
try:
    from balethon.proto import requests
except ImportError:
    pass


class RefreshToken:

    async def refresh_token(
            self: "balethon.Client"
    ) -> str:
        result = await self.execute(requests.GetJWTToken())
        self.save_session(result.jwt.value)
        return result.jwt.value
