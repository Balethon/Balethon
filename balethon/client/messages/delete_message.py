from typing import Union

import balethon
from ...objects import resolve_message_id


class DeleteMessage:

    async def delete_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            message_id = resolve_message_id(message_id)
            return await self.execute(requests.DeleteMessage(
                peer=structs.Peer(
                    type=peer_type,
                    id=peer_id
                ),
                rids=[message_id.rid],
                dates=structs.DeleteDates(dates=[message_id.date]),
                just_mine=False
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("deleteMessage", locals())
