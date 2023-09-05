import balethon
from ...objects import Message


class SendContact:

    async def send_contact(
            self: "balethon.Client",
            chat_id: int,
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendContact", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
