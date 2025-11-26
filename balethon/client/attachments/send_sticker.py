from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


class SendSticker:

    async def send_sticker(
            self: "balethon.Client",
            chat_id: Union[int, str],
            sticker: Union[str, bytes, BinaryIO, InputMedia],
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        sticker = resolve_media(sticker)
        return await self.auto_execute("sendSticker", locals())
