from typing import Union

import balethon
from ...objects import Message, resolve_message_id


class CopyMessage:

    async def copy_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            from_chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> Message:
        chat_id = await self.resolve_chat_id(chat_id)
        from_chat_id = await self.resolve_chat_id(from_chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            message_id = resolve_message_id(message_id)
            peer = structs.Peer(type=from_chat_id.peer_type, id=from_chat_id.peer_id)
            response = await self.execute(requests.LoadHistory(
                peer=peer,
                date=message_id.date,
                load_mode=2,
                limit=1
            ))
            result = response.history[0]
            return await self.execute(requests.SendMessage(
                peer=structs.Peer(type=chat_id.peer_type, id=chat_id.peer_id),
                rid=self.ws_connection.create_rid(),
                message=result.message,
                ex_peer=structs.Peer(type=chat_id.peer_type, id=chat_id.peer_id)
            ))

        return await self.auto_execute("copyMessage", locals())
