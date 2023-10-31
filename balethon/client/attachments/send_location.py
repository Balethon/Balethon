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
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("post", "sendLocation", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
