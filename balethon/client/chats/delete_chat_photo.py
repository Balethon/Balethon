from typing import Union

import balethon


class DeleteChatPhoto:

    async def delete_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import request_pb2, struct_pb2
            peer_id, peer_type = map(int, chat_id.split("|"))

            response = await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="LoadGroupAvatars",
                payload=request_pb2.LoadGroupAvatars(
                    peer=struct_pb2.GroupOutPeer(group_id=peer_id)
                )
            )

            avatars = response.avatars.avatars
            if not avatars:
                return
            last_avatar = avatars[0]

            return await self.invoke(
                service_name="bale.groups.v1.Groups",
                method="RemoveGroupAvatar",
                payload=request_pb2.RemoveGroupAvatar(
                    group_peer=struct_pb2.GroupOutPeer(group_id=peer_id, access_hash=1),
                    rid=self.ws_connection.create_rid(),
                    avatar_id=last_avatar.id
                )
            )

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("deleteChatPhoto", locals())
