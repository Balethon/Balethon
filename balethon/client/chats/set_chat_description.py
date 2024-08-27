from typing import Union

import balethon


class SetChatDescription:

    async def set_chat_description(
            self: "balethon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        return await self.execute("post", "setChatDescription", **data)
