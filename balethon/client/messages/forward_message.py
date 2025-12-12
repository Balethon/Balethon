from typing import Union

import balethon
from ...objects import Message
from balethon.proto import request_pb2, struct_pb2


class ForwardMessage:

    async def forward_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> Message:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            message_peer_id, message_peer_type = map(int, from_chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="ForwardMessages",
                payload=request_pb2.ForwardMessages(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=[self.connection.create_rid()],
                    forwarded_messages=[struct_pb2.HistoryMessageIdentifier(
                        peer=struct_pb2.Peer(type=message_peer_type, id=message_peer_id),
                        random_id=rid,
                        date=struct_pb2.Int64Value(date=date)
                    )]
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        from_chat_id = await self.resolve_peer_id(from_chat_id)
        return await self.auto_execute("forwardMessage", locals())
