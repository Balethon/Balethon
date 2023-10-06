import balethon
from ...objects import Object, Message
from balethon import objects


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: int,
            message_id: int,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        json = locals()
        del json["self"]
        for key, value in json.copy().items():
            if isinstance(value, Object):
                json[key] = value.unwrap()
        result = await self.connection.execute("post", "editMessageText", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
