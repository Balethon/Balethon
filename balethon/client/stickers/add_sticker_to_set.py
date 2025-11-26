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
        return await self.auto_execute("addStickerToSet", locals())
