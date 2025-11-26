from typing import Union

import balethon


class ExportChatInviteLink:

    async def export_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> str:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("exportChatInviteLink", locals())
