from typing import Union

import balethon
from ...objects import InviteLink


class RevokeChatInviteLink:

    async def revoke_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str],
            invite_link: str
    ) -> InviteLink:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.execute(requests.RevokeInviteUrl(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1)
            ))
            return InviteLink(link=response.url)

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("revokeChatInviteLink", locals())
