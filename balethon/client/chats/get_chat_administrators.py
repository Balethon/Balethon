import balethon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balethon.Client",
            chat_id: int
    ):
        data = locals()
        del data["self"]
        result = await self.execute("get", "getChatAdministrators", **data)
        result = [ChatMember.wrap(chat_administrator) for chat_administrator in result]
        for chat_administrator in result:
            chat_administrator.bind(self)
        return result
