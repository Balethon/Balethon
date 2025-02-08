from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int,
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("post", "editMessageText", locals())
