from typing import Union

import balethon


class UnpinChatMessage:

    async def unpin_chat_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int = None
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        return await self.execute("post", "unpinChatMessage", **data)
