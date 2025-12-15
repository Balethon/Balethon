from typing import Union

import balethon
from ...objects import Message
from balethon import objects
from balethon.proto import request_pb2, struct_pb2, response_pb2


class EditMessageCaption:

    async def edit_message_caption(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str],
            caption: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        if self.is_userbot():
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            peer = struct_pb2.Peer(type=peer_type, id=peer_id)
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
            result = response.history
            if not result:
                return
            result = result[0]
            result = result.message
            if result.document_message:
                result.document_message.caption.text = caption
            else:
                return
            return await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="UpdateMessage",
                payload=request_pb2.UpdateMessage(
                    peer=struct_pb2.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=rid,
                    updated_message=result
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageCaption", locals())
