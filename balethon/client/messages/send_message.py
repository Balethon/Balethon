import balethon
from ...objects import Message
from balethon import objects


class SendMessage:

    async def send_message(
            self: "balethon.Client",
            chat_id: int,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendMessage", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
