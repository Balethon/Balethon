from typing import Union

import balethon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("get", "getChatAdministrators", **data)
        result = [ChatMember.wrap(chat_administrator) for chat_administrator in result]
        for chat_administrator in result:
            chat_administrator.bind(self)
        return result
