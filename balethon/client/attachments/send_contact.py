from ...objects import Message


class SendContact:

    async def send_contact(self, chat_id, phone_number, first_name, last_name=None, reply_to_message_id=None):
        json = {"chat_id": chat_id, "phone_number": phone_number, "first_name": first_name, "last_name": last_name, "reply_to_message_id": reply_to_message_id}
        result = await self.connection.execute("post", "sendContact", json)
        return Message.wrap(result)
