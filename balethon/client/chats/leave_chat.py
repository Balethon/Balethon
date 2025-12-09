from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class LeaveChat:

    async def leave_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="LeaveGroup",
                payload=request_pb2.LeaveGroup(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    rid=self.connection.create_rid(),
                    make_orphan=False
                )
            )
        else:
            chat_id = await self.resolve_peer_id(chat_id)
            return await self.auto_execute("leaveChat", locals())
