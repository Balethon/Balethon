from typing import Union

import balethon


class AddStickerToSet:

    async def add_sticker_to_set(
            self: "balethon.Client",
            user_id: Union[int, str],
            name: str,
            sticker: str
    ) -> bool:
        user_id = await self.resolve_peer_id(user_id)
        data = locals()
        del data["self"]
        return await self.execute("get", "addStickerToSet", **data)
