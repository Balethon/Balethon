from typing import Union
from io import BufferedReader

import balethon
from ...objects import InputMediaAudio, Message


class SendVoice:

    async def send_voice(
            self: "balethon.Client",
            chat_id: int,
            voice: Union[str, bytes, BufferedReader],
            caption: str = None,
            duration: int = None,
            reply_to_message_id: int = None
    ):
        voice = InputMediaAudio(voice).media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVoice", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
