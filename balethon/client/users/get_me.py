import balethon
from ...objects import User


class GetMe:

    async def get_me(
            self: "balethon.Client"
    ) -> User:
        return await self.auto_execute("post", "getMe", locals())
