from typing import Union
from typing import BinaryIO

import balethon
from ...objects import InputMedia, Message


class SendDocument:

    async def send_document(
            self: "balethon.Client",
            chat_id: int,
            document: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_to_message_id: int = None
    ):
        if not isinstance(document, InputMedia):
            document = InputMedia(media=document)
        document = document.media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendDocument", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
