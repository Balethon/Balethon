from ...objects import Message


class EditMessageText:

    async def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text, "reply_markup": reply_markup}
        result = await self.connection.execute("post", "editMessageText", json)
        return Message.wrap(result)
