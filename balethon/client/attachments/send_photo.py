import balethon
from ...objects import Message


class SendPhoto:

    async def send_photo(
            self: "balethon.Client",
            chat_id: int,
            photo,
            caption: str = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendPhoto", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
