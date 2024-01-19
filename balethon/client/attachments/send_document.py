from typing import Union
from typing import BinaryIO

import balethon
from ...objects import Object, InputMedia, Message, ReplyMarkup


class SendDocument:

    async def send_document(
            self: "balethon.Client",
            chat_id: Union[int, str],
            document: Union[str, bytes, BinaryIO, InputMedia],
            caption: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        if not isinstance(document, InputMedia):
            document = InputMedia(media=document)
        document = document.media
        data = locals()
        del data["self"]
        for key, value in data.copy().items():
            if isinstance(value, Object):
                data[key] = value.unwrap()
        result = await self.execute("post", "sendDocument", json=False, **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
