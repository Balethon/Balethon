from typing import Union

import balethon
from ...objects import Message, resolve_message_id


class ForwardMessage:

    async def forward_message(
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
            return await self.execute(requests.ForwardMessages(
                peer=structs.Peer(type=chat_id.peer_type, id=chat_id.peer_id),
                rid=[self.ws_connection.create_rid()],
                forwarded_messages=[structs.HistoryMessageIdentifier(
                    peer=structs.OutPeer(type=from_chat_id.peer_type, id=from_chat_id.peer_id),
                    random_id=message_id.rid,
                    date=message_id.date
                )]
            ))

        return await self.auto_execute("forwardMessage", locals())
