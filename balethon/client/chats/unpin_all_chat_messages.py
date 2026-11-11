from typing import Union

import balethon


class UnpinAllChatMessages:

    async def unpin_all_chat_messages(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs

            if chat_id.peer_type in (1, 4):
                response = await self.execute(requests.LoadPinnedMessages(
                    peer=structs.ExPeer(type=chat_id.peer_type, id=chat_id.peer_id)
                ))

                message_ids = [
                    structs.MessageId(date=pinned_message.date, rid=pinned_message.rid)
                    for pinned_message in response.pinned_messages
                ]

                return await self.execute(requests.UnPinMessages(
                    peer=structs.ExPeer(type=chat_id.peer_type, id=chat_id.peer_id),
                    message_ids=message_ids,
                    all=True
                ))

            else:
                return await self.execute(requests.RemovePin(
                    group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id)
                ))

        return await self.auto_execute("unpinAllChatMessages", locals())
