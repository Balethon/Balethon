from typing import Union

import balethon
from ...objects import Message
from balethon import objects
from ...objects import resolve_message_id


class EditMessageCaption:

    async def edit_message_caption(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str],
            caption: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            message_id = resolve_message_id(message_id)
            peer = structs.Peer(type=chat_id.peer_type, id=chat_id.peer_id)
            response = await self.execute(requests.LoadHistory(
                peer=peer,
                date=message_id.date,
                load_mode=2,
                limit=1
            ))
            result = response.history[0].message
            return await self.execute(requests.UpdateMessage(
                peer=structs.Peer(
                    type=chat_id.peer_type,
                    id=chat_id.peer_id
                ),
                rid=message_id.rid,
                updated_message=result
            ))

        return await self.auto_execute("editMessageCaption", locals())
