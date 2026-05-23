from typing import Union

import balethon


class UnpinAllChatMessages:

    async def unpin_all_chat_messages(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))

            if peer_type in (1, 4):
                response = await self.execute(requests.LoadPinnedMessages(
                    peer=structs.ExPeer(type=peer_type, id=peer_id)
                ))

                message_ids = [
                    structs.MessageId(date=pinned_message.date, rid=pinned_message.rid)
                    for pinned_message in response.pinned_messages
                ]

                return await self.execute(requests.UnPinMessages(
                    peer=structs.ExPeer(type=peer_type, id=peer_id),
                    message_ids=message_ids,
                    all=True
                ))

            elif peer_type in (2, 3, 5):
                return await self.execute(requests.RemovePin(
                    group_peer=structs.GroupOutPeer(group_id=peer_id)
                ))

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("unpinAllChatMessages", locals())
