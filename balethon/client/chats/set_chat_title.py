from typing import Union

import balethon


class SetChatTitle:

    async def set_chat_title(
            self: "balethon.Client",
            chat_id: Union[int, str],
            title: str
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("setChatTitle", locals())
