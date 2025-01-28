from typing import Union

import balethon
from ...objects import Message


class SendLocation:

    async def send_location(
            self: "balethon.Client",
            chat_id: Union[int, str],
            latitude: int,
            longitude: int,
            reply_to_message_id: int = None
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("post", "sendLocation", locals())
