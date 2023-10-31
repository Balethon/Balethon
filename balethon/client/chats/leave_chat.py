from typing import Union

import balethon


class LeaveChat:

    async def leave_chat(
            self: "balethon.Client",
            chat_id: Union[int, str]
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        return await self.execute("post", "leaveChat", **data)
