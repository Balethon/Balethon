import balethon
from ...objects import User


class GetMe:

    async def get_me(
            self: "balethon.Client"
    ) -> User:
        if self.is_userbot():
            my_id = self.session["id"]
            return await self.get_chat(f"{my_id}|1")

        return await self.auto_execute("getMe", locals())
