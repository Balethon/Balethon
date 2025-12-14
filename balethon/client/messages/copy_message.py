from typing import Union

import balethon
from ...objects import Message
from balethon.proto import request_pb2, struct_pb2, response_pb2


class CopyMessage:

    async def copy_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> Message:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            from_peer_id, from_peer_type = map(int, from_chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            peer = struct_pb2.Peer(type=from_peer_type, id=from_peer_id)
            response = await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="LoadHistory",
                payload=request_pb2.LoadHistory(
                    peer=peer,
                    date=date,
                    load_mode=2,
                    limit=1
                )
            )
            result = response_pb2.LoadHistory()
            result.ParseFromString(response)
            result = result.history
            if not result:
                return
            result = result[0]
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMessage",
                payload=request_pb2.SendMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=self.connection.create_rid(),
                    message=result.message,
                    ex_peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        from_chat_id = await self.resolve_peer_id(from_chat_id)
        return await self.auto_execute("copyMessage", locals())
