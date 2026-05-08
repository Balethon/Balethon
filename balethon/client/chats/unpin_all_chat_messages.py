from typing import Union

import balethon


class UnpinAllChatMessages:

    async def unpin_all_chat_messages(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import request_pb2, struct_pb2
            peer_id, peer_type = map(int, chat_id.split("|"))

            if peer_type in (1, 4):
                response = await self.invoke(
                    service_name="bale.messaging.v2.Messaging",
                    method="LoadPinnedMessages",
                    payload=request_pb2.LoadPinnedMessages(
                        peer=struct_pb2.ExPeer(type=peer_type, id=peer_id)
                    )
                )

                message_ids = [
                    struct_pb2.MessageId(date=pinned_message.date, rid=pinned_message.rid)
                    for pinned_message in response.pinned_messages
                ]

                return await self.invoke(
                    service_name="bale.messaging.v2.Messaging",
                    method="UnPinMessages",
                    payload=request_pb2.UnPinMessages(
                        peer=struct_pb2.ExPeer(type=peer_type, id=peer_id),
                        message_ids=message_ids,
                        all=True
                    )
                )

            elif peer_type in (2, 3, 5):
                return await self.invoke(
                    service_name="bale.groups.v1.Groups",
                    method="RemovePin",
                    payload=request_pb2.RemovePin(
                        group_peer=struct_pb2.GroupOutPeer(group_id=peer_id)
                    )
                )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("unpinAllChatMessages", locals())
