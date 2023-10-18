from typing import Union
from os.path import isfile

import balethon
from ...objects import Message


class SendVideo:

    async def send_video(
            self: "balethon.Client",
            chat_id: int,
            video: Union[str, bytes],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_to_message_id: int = None
    ):
        if isfile(video):
            with open(video, "rb") as video_file:
                video = video_file.read()
        del video_file
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendVideo", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
