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
        data = locals()
        del data["self"]
        result = await self.execute("post", "revokeChatInviteLink", **data)
        result = InviteLink.wrap(result)
        result.bind(chat_id)
        return result
