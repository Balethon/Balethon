from typing import Union, List

import balethon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> List[ChatMember]:
        if self.is_userbot():
            result = await self.get_chat_members(chat_id)
            return [member for member in result.members if member.is_admin.value]

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatAdministrators", locals())
