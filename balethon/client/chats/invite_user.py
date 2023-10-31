from typing import Union

import balethon


class InviteUser:

    async def invite_user(
            self: "balethon.Client",
            chat_id: Union[int, str],
            user_id: Union[int, str]
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        user_id = await self.resolve_peer_id(user_id)
        data = locals()
        del data["self"]
        return await self.execute("post", "inviteUser", **data)
