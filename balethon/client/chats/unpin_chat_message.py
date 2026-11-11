from typing import Union

import balethon
from ...objects import resolve_message_id


class UnpinChatMessage:

    async def unpin_chat_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            message_id = resolve_message_id(message_id)

            if chat_id.peer_type in (1, 4):
                return await self.execute(requests.UnPinMessages(
                    peer=structs.ExPeer(type=chat_id.peer_type, id=chat_id.peer_id),
                    message_ids=[structs.MessageId(date=message_id.date, rid=message_id.rid)]
                ))

            else:
                return await self.execute(requests.RemoveSinglePin(
                    group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id),
                    rid=message_id.rid,
                    date=message_id.date
                ))

        return await self.auto_execute("unpinChatMessage", locals())
