from typing import Union

import balethon
from ...objects import Message
from balethon import objects
from balethon.proto import request_pb2, struct_pb2


class SendMessage:

    async def send_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None,
            reply_to_message_id: int = None
    ) -> Message:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="SendMessage",
                payload=request_pb2.SendMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=self.connection.create_rid(),
                    message=struct_pb2.Message(
                        text_message=struct_pb2.TextMessage(
                            text=text
                        )
                    ),
                    ex_peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    )
                )
            )
        else:
            chat_id = await self.resolve_peer_id(chat_id)
            return await self.auto_execute("sendMessage", locals())
