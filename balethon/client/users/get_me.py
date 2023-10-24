import balethon
from ...objects import User


class GetMe:

    async def get_me(
            self: "balethon.Client"
    ):
        result = await self.execute("get", "getMe")
        result = User.wrap(result)
        result.bind(self)
        return result
