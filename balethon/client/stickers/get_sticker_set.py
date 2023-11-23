import balethon
from ...objects import StickerSet


class GetStickerSet:

    async def get_sticker_set(
            self: "balethon.Client",
            name: str
    ) -> StickerSet:
        data = locals()
        del data["self"]
        result = await self.execute("get", "getStickerSet", **data)
        result = StickerSet.wrap(result)
        result.bind(self)
        return result
