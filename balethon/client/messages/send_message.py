from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class SendMessage:

    async def send_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("sendMessage", locals())
