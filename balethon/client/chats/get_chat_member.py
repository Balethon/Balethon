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
        data = locals()
        del data["self"]
        result = await self.execute("get", "getChatMember", **data)
        result = ChatMember.wrap(result)
        result.bind(self)
        return result
