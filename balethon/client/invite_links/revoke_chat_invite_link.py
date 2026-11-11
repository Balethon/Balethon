from typing import Union

import balethon
from ...objects import InviteLink


class RevokeChatInviteLink:

    async def revoke_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str],
            invite_link: str
    ) -> InviteLink:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            response = await self.execute(requests.RevokeInviteUrl(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1)
            ))
            return InviteLink(link=response.url)

        return await self.auto_execute("revokeChatInviteLink", locals())
