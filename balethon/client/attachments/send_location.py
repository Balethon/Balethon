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
        json = locals()
        del json["self"]
        result = await self.execute("post", "sendLocation", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
