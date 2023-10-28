from typing import Union
from io import BufferedReader

import balethon
from ...objects import InputMediaAudio, Message


class SendAudio:

    async def send_audio(
            self: "balethon.Client",
            chat_id: int,
            audio: Union[str, bytes, BufferedReader],
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_to_message_id: int = None
    ):
        audio = InputMediaAudio(audio).media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendAudio", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
