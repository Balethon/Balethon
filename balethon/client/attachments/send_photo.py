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
        del data["self"]
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        result = await self.execute("post", "sendPhoto", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
