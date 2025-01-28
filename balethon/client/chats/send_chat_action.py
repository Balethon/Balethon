from typing import Union

import balethon


class SendChatAction:

    async def send_chat_action(
            self: "balethon.Client",
            chat_id: Union[int, str],
            action: str = "typing"
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        chat_id = str(chat_id)  # The sendChatAction method only works with a string chat_id
        return await self.auto_execute("post", "sendChatAction", locals())
