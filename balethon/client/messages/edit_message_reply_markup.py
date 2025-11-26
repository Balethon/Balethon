from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class EditMessageReplyMarkup:

    async def edit_message_reply_markup(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int,
            reply_markup: "objects.ReplyMarkup"
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageReplyMarkup", locals())
