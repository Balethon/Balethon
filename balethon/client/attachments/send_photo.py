from typing import Union
from os.path import isfile

import balethon
from ...objects import Message


class SendPhoto:

    async def send_photo(
            self: "balethon.Client",
            chat_id: int,
            photo: Union[str, bytes],
            caption: str = None,
            reply_to_message_id: int = None
    ):
        if isfile(photo):
            with open(photo, "rb") as photo_file:
                photo = photo_file.read()
                del photo_file
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendPhoto", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
