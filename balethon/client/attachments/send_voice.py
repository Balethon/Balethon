from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendVoice:

    async def send_voice(
            self: "balethon.Client",
            chat_id: Union[int, str],
            voice: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            duration: int = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(voice, InputMedia):
            voice = InputMedia(media=voice)
        voice = voice.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVoice", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
