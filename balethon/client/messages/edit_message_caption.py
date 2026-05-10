from typing import Union

import balethon
from ...objects import Message
from balethon import objects


class EditMessageCaption:

    async def edit_message_caption(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str],
            caption: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))
            peer = structs.Peer(type=peer_type, id=peer_id)
            response = await self.invoke(
                service_name="bale.messaging.v2.Messaging",
                method="LoadHistory",
                payload=requests.LoadHistory(
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
                payload=requests.UpdateMessage(
                    peer=structs.Peer(
                        type=peer_type,
                        id=peer_id
                    ),
                    rid=rid,
                    updated_message=result
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageCaption", locals())
