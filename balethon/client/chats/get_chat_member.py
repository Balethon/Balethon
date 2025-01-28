from typing import Union

import balethon
from ...objects import ChatMember


class GetChatMember:

    async def get_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ) -> ChatMember:
        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("get", "getChatMember", locals())
