from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class UnpinChatMessage:

    async def unpin_chat_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="UnpinMessages",
                payload=request_pb2.UnPinMessages(
                    peer=struct_pb2.ExPeer(type=peer_type, id=peer_id, access_hash=1),
                    message_ids=[struct_pb2.MessageId(date=date, rid=rid)]
                )
            )
        else:
            chat_id = await self.resolve_peer_id(chat_id)
            return await self.auto_execute("unpinChatMessage", locals())
