from typing import Union

import balethon


class DeleteChatPhoto:

    async def delete_chat_photo(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs, enums

            if chat_id.peer_id == self.user.id:
                response = await self.execute(requests.LoadAvatars(
                    peer=structs.UserOutPeer(uid=chat_id.peer_id, access_hash=1))
                )
            else:
                response = await self.execute(requests.LoadGroupAvatars(
                    peer=structs.GroupOutPeer(group_id=chat_id.peer_id)
                ))

            last_avatar = response.avatars.avatars[0]

            if chat_id.peer_id == self.user.id:
                return await self.execute(requests.RemoveAvatar(avatar_id=last_avatar.id))

            return await self.execute(requests.RemoveGroupAvatar(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                rid=self.ws_connection.create_rid(),
                avatar_id=last_avatar.id
            ))

        return await self.auto_execute("deleteChatPhoto", locals())
