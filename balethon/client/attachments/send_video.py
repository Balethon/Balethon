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
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVideo", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
