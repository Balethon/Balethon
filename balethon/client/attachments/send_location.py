from ...objects import Message


class SendLocation:

    async def send_location(self, chat_id, latitude, longitude, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendLocation", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
