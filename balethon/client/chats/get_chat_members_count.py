from typing import Union

import balethon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> int:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatMembersCount", locals())
