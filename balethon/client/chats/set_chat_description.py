from typing import Union

import balethon


class SetChatDescription:

    async def set_chat_description(
            self: "balethon.Client",
            chat_id: Union[int, str],
            description: str
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatDescription", locals())
