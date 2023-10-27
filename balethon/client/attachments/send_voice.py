from typing import Union
from os.path import isfile

import balethon
from ...objects import Message


class SendVoice:

    async def send_voice(
            self: "balethon.Client",
            chat_id: int,
            voice: Union[str, bytes],
            caption: str = None,
            duration: int = None,
            reply_to_message_id: int = None
    ):
        if isfile(voice):
            with open(voice, "rb") as voice_file:
                voice = voice_file.read()
                del voice_file
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVoice", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
