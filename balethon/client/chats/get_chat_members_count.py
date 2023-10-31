from typing import Union

import balethon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        return await self.execute("get", "getChatMembersCount", **data)
