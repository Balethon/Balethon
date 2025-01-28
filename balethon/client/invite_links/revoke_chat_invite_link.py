from typing import Union

import balethon
from ...objects import InviteLink


class RevokeChatInviteLink:

    async def revoke_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str],
            invite_link: str
    ) -> InviteLink:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("post", "revokeChatInviteLink", locals())
