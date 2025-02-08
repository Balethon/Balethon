from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendAnimation:

    async def send_animation(
            self: "balethon.Client",
            chat_id: Union[int, str],
            animation: Union[str, bytes, BinaryIO, InputMedia],
            duration: int = None,
            width: int = None,
            height: int = None,
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        animation = resolve_media(animation)
        return await self.auto_execute(
            "post",
            "sendAnimation",
            locals(),
            json=False,  # The sendAnimation method only works with multipart/form-data
        )
