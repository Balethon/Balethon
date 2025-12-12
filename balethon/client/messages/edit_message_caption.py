from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class EditMessageCaption:

    async def edit_message_caption(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int,
            caption: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        if self.is_userbot():
            return await self.edit_message_text(chat_id, message_id, caption)
        
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageCaption", locals())
