from typing import Union

import balethon


class UnpinChatMessage:

    async def unpin_chat_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            rid, date = map(int, message_id.split("|"))

            if peer_type in (1, 4):
                return await self.execute(requests.UnPinMessages(
                    peer=structs.ExPeer(type=peer_type, id=peer_id),
                    message_ids=[structs.MessageId(date=date, rid=rid)]
                ))

            elif peer_type in (2, 3, 5):
                return await self.execute(requests.RemoveSinglePin(
                    group_peer=structs.GroupOutPeer(group_id=peer_id),
                    rid=rid,
                    date=date
                ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("unpinChatMessage", locals())
