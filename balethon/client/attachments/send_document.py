from typing import Union, BinaryIO

import balethon
from ...objects import InputMedia, resolve_media, Message, ReplyMarkup


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
        document = resolve_media(document)
        return await self.auto_execute("post", "sendDocument", locals())
