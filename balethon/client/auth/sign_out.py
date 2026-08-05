import balethon
try:
    from balethon.proto import requests
except ImportError:
    pass


class SignOut:

    async def sign_out(
            self: "balethon.Client"
    ):
        await self.execute(requests.SignOut())
