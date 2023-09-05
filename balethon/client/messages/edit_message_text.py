import balethon
from ...objects import Message


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: int,
            message_id: int,
            text: str,
            reply_markup=None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "editMessageText", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
