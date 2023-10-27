import balethon
from ...objects import Message


class ForwardMessage:

    async def forward_message(
            self: "balethon.Client",
            chat_id: int,
            from_chat_id: int,
            message_id: int
    ):
        data = locals()
        del data["self"]
        result = await self.execute("post", "forwardMessage", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
