from typing import Union

import balethon


class BanChatMember:

    async def ban_chat_member(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ) -> bool:
        chat_id = await self.resolve_chat_id(chat_id)
        user_id = await self.resolve_chat_id(user_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            return await self.execute(requests.KickUser(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
                user=structs.UserOutPeer(uid=user_id, access_hash=1),
                rid=self.ws_connection.create_rid()
            ))

        return await self.auto_execute("banChatMember", locals())
