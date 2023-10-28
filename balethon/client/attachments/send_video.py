from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendVideo:

    async def send_video(
            self: "balethon.Client",
            chat_id: int,
            video: Union[str, bytes, BinaryIO, InputMedia],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_to_message_id: int = None
    ):
        if not isinstance(video, InputMedia):
            video = InputMedia(media=video)
        video = video.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendVideo", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
