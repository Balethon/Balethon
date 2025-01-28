from typing import Union, BinaryIO

import balethon
from ...objects import Object, InputMedia, Message, ReplyMarkup


class SendSticker:

    async def send_sticker(
            self: "balethon.Client",
            chat_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(sticker, InputMedia):
            sticker = InputMedia(media=sticker)
        sticker = sticker.media
        data = locals()
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        return await self.auto_execute("post", "sendSticker", data)
