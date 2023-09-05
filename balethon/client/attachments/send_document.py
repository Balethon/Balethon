import balethon
from ...objects import Message


class SendDocument:

    async def send_document(
            self: "balethon.Client",
            chat_id: int,
            document,
            caption: str = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendDocument", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
