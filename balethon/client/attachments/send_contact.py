from typing import Union

import balethon
from ...objects import Message


class SendContact:

    async def send_contact(
            self: "balethon.Client",
            chat_id: Union[int, str],
            phone_number: str,
            first_name: str,
            last_name: str = None,
            reply_to_message_id: int = None
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendContact", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
