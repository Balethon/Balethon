from typing import Union
from io import BufferedReader

import balethon
from ...objects import InputMediaDocument, Message


class SendDocument:

    async def send_document(
            self: "balethon.Client",
            chat_id: int,
            document: Union[str, bytes, BufferedReader],
            caption: str = None,
            reply_to_message_id: int = None
    ):
        document = InputMediaDocument(document).media
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendDocument", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
