import balethon
from ...objects import ChatMember


class GetChatMember:

    async def get_chat_member(
            self: "balethon.Client",
            chat_id: int,
            user_id: int
    ):
        data = locals()
        del data["self"]
        result = await self.execute("get", "getChatMember", **data)
        result = ChatMember.wrap(result)
        result.bind(self)
        return result
