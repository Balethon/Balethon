from typing import Union

import balethon
from ...objects import InviteLink
from balethon.proto import request_pb2, struct_pb2, response_pb2


class RevokeChatInviteLink:

    async def revoke_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str],
            invite_link: str
    ) -> InviteLink:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="RevokeInviteURL",
                payload=request_pb2.RevokeInviteUrl(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1)
                )
            )
            return InviteLink(link=response.url)

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("revokeChatInviteLink", locals())
