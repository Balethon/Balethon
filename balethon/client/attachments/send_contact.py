from typing import Union

import balethon
from ...objects import Message, ReplyMarkup


class SendContact:

    async def send_contact(
            self: "balethon.Client",
            chat_id: Union[int, str],
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_markup: ReplyMarkup = None,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("sendContact", locals())
