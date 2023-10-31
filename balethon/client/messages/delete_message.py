from typing import Union

import balethon


class DeleteMessage:

    async def delete_message(
            self: "balethon.Client",
            chat_id: Union[int, str],
            message_id: int
    ):
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        del data["self"]
        return await self.execute("get", "deleteMessage", **data)
