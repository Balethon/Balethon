import balethon
from ...objects import Message


class SendVoice:

    async def send_voice(
            self: "balethon.Client",
            chat_id: int,
            voice,
            caption: str = None,
            duration: int = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendVoice", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
