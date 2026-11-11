from typing import Union

import balethon


class ExportChatInviteLink:

    async def export_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> str:
        chat_id = await self.resolve_chat_id(chat_id)

        if self.is_userbot():
            from balethon.proto import requests, structs
            response = await self.execute(requests.GetGroupInviteUrl(
                group_peer=structs.GroupOutPeer(group_id=chat_id.peer_id, access_hash=1)
            ))
            return response.url

        return await self.auto_execute("exportChatInviteLink", locals())
