from typing import Union
from io import BufferedReader

import balethon
from ...objects import InputMediaVideo, Message


class SendVideo:

    async def send_video(
            self: "balethon.Client",
            chat_id: int,
            video: Union[str, bytes, BufferedReader],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_to_message_id: int = None
    ):
        video = InputMediaVideo(video).media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVideo", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
