import balethon
from ...objects import Message


class SendLocation:

    async def send_location(
            self: "balethon.Client",
            chat_id: int,
            latitude: int,
            longitude: int,
            reply_to_message_id: int = None
    ):
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendLocation", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
