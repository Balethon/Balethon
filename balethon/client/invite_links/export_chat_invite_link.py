from typing import Union

import balethon


class ExportChatInviteLink:

    async def export_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> str:
        if self.is_userbot():
            from balethon.proto import requests, structs
            peer_id, peer_type = map(int, chat_id.split("|"))
            response = await self.execute(requests.GetGroupInviteUrl(
                group_peer=structs.GroupOutPeer(group_id=peer_id, access_hash=1)
            ))
            return response.url

        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("exportChatInviteLink", locals())
