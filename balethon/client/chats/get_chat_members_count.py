from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2, response_pb2


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> int:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="GetGroupMembersCount",
                payload=request_pb2.GetGroupMembersCount(
                    group=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                )
            )
            result = response_pb2.GetGroupMembersCount()
            result.ParseFromString(response)
            return result.members_count
        
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("getChatMembersCount", locals())
