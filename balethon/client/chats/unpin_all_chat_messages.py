from typing import Union

import balethon


class UnpinAllChatMessages:

    async def unpin_all_chat_messages(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("unpinAllChatMessages", locals())
