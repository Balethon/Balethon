from typing import Union

import balethon
from ...objects import Message


class ForwardMessage:

    async def forward_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            from_chat_id: int,
            message_id: int
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("post", "forwardMessage", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
