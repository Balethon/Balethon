from typing import Union, BinaryIO

import balethon
from ...objects import Object, InputMedia, Message, ReplyMarkup


class SendPhoto:

    async def send_photo(
            self: "balethon.Client",
            chat_id: Union[int, str],
            photo: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(photo, InputMedia):
            photo = InputMedia(media=photo)
        photo = photo.media
        data = locals()
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        return await self.auto_execute("post", "sendPhoto", data)
