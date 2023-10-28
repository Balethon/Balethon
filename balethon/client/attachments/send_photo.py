from typing import Union
from io import BufferedReader

import balethon
from ...objects import InputMediaPhoto, Message


class SendPhoto:

    async def send_photo(
            self: "balethon.Client",
            chat_id: int,
            photo: Union[str, bytes, BufferedReader],
            caption: str = None,
            reply_to_message_id: int = None
    ):
        photo = InputMediaPhoto(photo).media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendPhoto", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
