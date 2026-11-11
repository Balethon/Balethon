from typing import Union

import balethon


class GetChatMembersCount:

    async def get_chat_members_count(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> int:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            response = await self.execute(requests.GetGroupMembersCount(
                group=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1),
            ))
            return response.members_count

        return await self.auto_execute("getChatMembersCount", locals())
