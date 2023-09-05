import balethon
from ...objects import Message


class SendAudio:

    async def send_audio(
            self: "balethon.Client",
            chat_id: int,
            audio,
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_to_message_id: int = None
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendAudio", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
