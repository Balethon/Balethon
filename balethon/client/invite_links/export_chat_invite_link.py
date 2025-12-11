from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2, response_pb2


class ExportChatInviteLink:

    async def export_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> str:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="GetGroupInviteURL",
                payload=request_pb2.GetGroupInviteUrl(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1)
                )
            )
            result = response_pb2.GetGroupInviteUrl()
            result.ParseFromString(response)
            return result.url

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("exportChatInviteLink", locals())
