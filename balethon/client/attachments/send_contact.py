from ...objects import Message


class SendContact:

    async def send_contact(self, chat_id, phone_number, first_name, last_name=None, reply_to_message_id=None):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendContact", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
