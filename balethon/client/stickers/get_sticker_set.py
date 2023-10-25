import balethon


class GetStickerSet:

    async def get_sticker_set(
            self: "balethon.Client",
            name: str
    ):
        json = locals()
        del json["self"]
        return await self.execute("get", "getStickerSet", json)
