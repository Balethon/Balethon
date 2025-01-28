import balethon
from ...objects import StickerSet


class GetStickerSet:

    async def get_sticker_set(
            self: "balethon.Client",
            name: str
    ) -> StickerSet:
        return await self.auto_execute("get", "getStickerSet", locals())
