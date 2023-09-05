from ...objects import Message


class SendMessage:

    async def send_message(self, chat_id, text, reply_markup=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendMessage", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
