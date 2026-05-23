from typing import Union

import balethon
from ...objects import Message
from balethon import objects
from ...objects import resolve_message_id


class EditMessageText:

    async def edit_message_text(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str],
            text: str,
            reply_markup: "objects.ReplyMarkup" = None
    ) -> Message:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            message_id = resolve_message_id(message_id)
            peer = structs.Peer(type=peer_type, id=peer_id)
            response = await self.execute(requests.LoadHistory(
                peer=peer,
                date=message_id.date,
                load_mode=2,
                limit=1
            ))
            result = response.history[0].message
            return await self.execute(requests.UpdateMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rid=message_id.rid,
                updated_message=result
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageText", locals())
