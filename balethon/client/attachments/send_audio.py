from typing import Union
from os.path import isfile

import balethon
from ...objects import Message


class SendAudio:

    async def send_audio(
            self: "balethon.Client",
            chat_id: int,
            audio: Union[str, bytes],
            caption: str = None,
            duration: int = None,
            title: str = None,
            reply_to_message_id: int = None
    ):
        if isfile(audio):
            with open(audio, "rb") as audio_file:
                audio = audio_file.read()
                del audio_file
        json = locals()
        del json["self"]
        result = await self.execute("post", "sendAudio", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
