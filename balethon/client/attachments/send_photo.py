from ...objects import Message


class SendPhoto:

    async def send_photo(self, chat_id, photo, caption=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendPhoto", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
