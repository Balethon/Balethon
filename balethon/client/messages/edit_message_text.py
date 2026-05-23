from typing import Union

import balethon
from ...objects import Message
from balethon import objects


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
            rid, date = map(int, message_id.split("|"))
            peer = structs.Peer(type=peer_type, id=peer_id)
            response = await self.execute(requests.LoadHistory(
                peer=peer,
                date=date,
                load_mode=2,
                limit=1
            ))
            result = response.history
            if not result:
                return
            result = result[0]
            result = result.message
            if result.text_message:
                result.text_message.text = text
            else:
                return
            return await self.execute(requests.UpdateMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rid=rid,
                updated_message=result
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("editMessageText", locals())
