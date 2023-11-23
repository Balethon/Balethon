from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendAnimation:

    async def send_animation(
            self: "balethon.Client",
            chat_id: Union[int, str],
            animation: Union[str, bytes, BinaryIO, InputMedia],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(animation, InputMedia):
            animation = InputMedia(media=animation)
        animation = animation.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendAnimation", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
