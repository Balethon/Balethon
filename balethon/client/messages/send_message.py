import balethon
from ...objects import Object, Message
from balethon import objects


class SendMessage:

    async def send_message(
            self: "balethon.Client",
            chat_id: int,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None
    ):
        for value in locals().values():
            if isinstance(value, Object):
                value.unwrap()
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendMessage", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
