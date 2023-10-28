from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendVoice:

    async def send_voice(
            self: "balethon.Client",
            chat_id: int,
            voice: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            duration: int = None,
            reply_to_message_id: int = None
    ):
        if not isinstance(voice, InputMedia):
            voice = InputMedia(media=voice)
        voice = voice.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVoice", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
