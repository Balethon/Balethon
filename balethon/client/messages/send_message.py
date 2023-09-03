from ...objects import Message


class SendMessage:

    async def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendMessage", json)
        return Message.wrap(result)
