class EditMessageText:

    async def edit_message_text(self, chat_id, message_id, text, reply_markup=None):
        json = {"chat_id": chat_id, "message_id": message_id, "text": text, "reply_markup": reply_markup}
        return await self.connection.execute("post", "editMessageText", json)
