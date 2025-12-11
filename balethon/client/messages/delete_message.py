from typing import Union

import balethon
from balethon.proto import request_pb2, struct_pb2


class DeleteMessage:

    async def delete_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="DeleteMessage",
                payload=request_pb2.DeleteMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rids=[rid],
                    dates=struct_pb2.DeleteDates(dates=[date]),
                    just_mine=False
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("deleteMessage", locals())
