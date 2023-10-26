import balethon
from ...objects import StickerSet


class GetStickerSet:

    async def get_sticker_set(
            self: "balethon.Client",
            name: str
    ):
        json = locals()
        del json["self"]
        result = await self.execute("get", "getStickerSet", json)
        print(result)
        result = StickerSet.wrap(result)
        result.bind(self)
        return result
