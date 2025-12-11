from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class PinChatMessage:

    async def pin_chat_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            if peer_type in (1, 4):
                return await self.invoke(
                    service_name="bale.messaging.v2.Messaging",
                    method="PinMessages",
                    payload=request_pb2.PinMessages(
                        peer=struct_pb2.ExPeer(type=peer_type, id=peer_id, access_hash=1),
                        message_id=struct_pb2.MessageId(date=date, rid=rid)
                    )
                )
            elif peer_type in (2 ,3 ,5):
                return await self.invoke(
                    service_name="bale.groups.v1.Groups",
                    method="PinMessage",
                    payload=request_pb2.PinMessage(
                        group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                        date=date,
                        msg_rid=rid
                    )
                )
        else:
            chat_id = await self.resolve_peer_id(chat_id)
            return await self.auto_execute("pinChatMessage", locals())
