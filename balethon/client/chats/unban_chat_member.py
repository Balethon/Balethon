from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class UnbanChatMember:

    async def unban_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str],
            only_if_banned: bool = True
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="UnBanUser",
                payload=request_pb2.UnBanUser(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    user=struct_pb2.UserOutPeer(uid=user_id, access_hash=1)
                )
            )
        else:
            chat_id = await self.resolve_peer_id(chat_id)
            user_id = await self.resolve_peer_id(user_id)
            return await self.auto_execute("unbanChatMember", locals())
