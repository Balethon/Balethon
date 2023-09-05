from ...objects import Message


class SendDocument:

    async def send_document(self, chat_id, document, caption=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendDocument", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
