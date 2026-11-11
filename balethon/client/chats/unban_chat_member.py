from typing import Union

import balethon


class UnbanChatMember:

    async def unban_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str],
            only_if_banned: bool = True
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)
        user_id = await self.resolve_chat_id(user_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            return await self.execute(requests.UnBanUser(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                user=structs.UserOutPeer(uid=user_id.peer_id, access_hash=1)
            ))

        return await self.auto_execute("unbanChatMember", locals())
