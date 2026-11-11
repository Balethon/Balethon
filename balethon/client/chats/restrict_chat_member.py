from typing import Union

import balethon
from balethon import objects


class RestrictChatMember:

    async def restrict_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str],
            permissions: "objects.ChatPermissions"
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)
        user_id = await self.resolve_chat_id(user_id)

        if self.is_userbot():
            from ...proto import requests, structs
            return await self.execute(requests.RemoveUserAdmin(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                user_peer=structs.UserOutPeer(uid=user_id.peer_id, access_hash=1),
            ))

        return await self.auto_execute("restrictChatMember", locals())
