from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message, ReplyMarkup


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
        result = await self.execute("post", "sendPhoto", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
