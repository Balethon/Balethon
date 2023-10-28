from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendAudio:

    async def send_audio(
            self: "balethon.Client",
            chat_id: int,
            audio: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_to_message_id: int = None
    ):
        if not isinstance(audio, InputMedia):
            audio = InputMedia(media=audio)
        audio = audio.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendAudio", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
