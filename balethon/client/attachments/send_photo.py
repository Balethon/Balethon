from ...objects import Message


class SendPhoto:

    async def send_photo(self, chat_id, photo, caption=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "photo": photo, "caption": caption, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendPhoto", json)
        return Message.wrap(result)
