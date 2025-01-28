from typing import Union

import balethon


class DeleteMessage:

    async def delete_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int
    ) -> bool:
        chat_id = await self.resolve_peer_id(chat_id)
        return await self.auto_execute("get", "deleteMessage", locals())
