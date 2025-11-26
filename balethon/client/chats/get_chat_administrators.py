from typing import Union, List

import balethon
from ...objects import ChatMember


class GetChatAdministrators:

    async def get_chat_administrators(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> List[ChatMember]:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatAdministrators", locals())
