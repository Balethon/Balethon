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
        return await self.auto_execute("post", "copyMessage", locals())
