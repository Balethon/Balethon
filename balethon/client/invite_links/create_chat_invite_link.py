from typing import Union

import balethon
from ...objects import InviteLink


class CreateChatInviteLink:

    async def create_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> InviteLink:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("post", "createChatInviteLink", locals())
