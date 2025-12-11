from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class BanChatMember:

    async def ban_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="KickUser",
                payload=request_pb2.KickUser(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    user=struct_pb2.UserOutPeer(uid=user_id, access_hash=1),
                    rid=self.connection.create_rid()
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("banChatMember", locals())
