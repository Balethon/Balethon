from typing import Union

import balethon
from ...objects import InviteLink


class CreateChatInviteLink:

    async def create_chat_invite_link(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ) -> InviteLink:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        result = await self.execute("post", "createChatInviteLink", **data)
        result = InviteLink.wrap(result)
        result.bind(chat_id)
        return result
