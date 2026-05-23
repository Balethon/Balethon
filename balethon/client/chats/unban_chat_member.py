from typing import Union

import balethon


class UnbanChatMember:

    async def unban_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str],
            only_if_banned: bool = True
    ) -> bool:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            return await self.execute(requests.UnBanUser(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1),
                user=structs.UserOutPeer(uid=user_id, access_hash=1)
            ))

        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        return await self.auto_execute("unbanChatMember", locals())
