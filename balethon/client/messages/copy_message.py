from typing import Union

import balethon
from ...objects import Message


class CopyMessage:

    async def copy_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: int
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        from_chat_id = await self.resolve_peer_id(from_chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("post", "copyMessage", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
