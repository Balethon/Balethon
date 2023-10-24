from typing import Union
from os.path import isfile

import balethon
from ...objects import Message


class SendDocument:

    async def send_document(
            self: "balethon.Client",
            chat_id: int,
            document: Union[str, bytes],
            caption: str = None,
            reply_to_message_id: int = None
    ):
        if isfile(document):
            with open(document, "rb") as document_file:
                document = document_file.read()
        del document_file
        json = locals()
        del json["self"]
        result = await self.execute("post", "sendDocument", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
