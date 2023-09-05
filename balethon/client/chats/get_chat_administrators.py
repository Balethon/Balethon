import balethon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balethon.Client",
            chat_id: int
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("get", "getChatAdministrators", json)
        result = [ChatMember.wrap(chat_administrator) for chat_administrator in result]
        for chat_administrator in result:
            chat_administrator.bind(self)
        return result
