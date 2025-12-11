from typing import Union

import balethon
from ...objects import Message
from balethon import objects
from balethon.proto import request_pb2, struct_pb2


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="UpdateMessage",
                payload=request_pb2.UpdateMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=rid,
                    updated_message=struct_pb2.Message(
                        text_message=struct_pb2.TextMessage(
                            text=text
                        )
                    )
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageText", locals())
