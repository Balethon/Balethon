import balethon


class CreateNewStickerSet:

    async def create_new_sticker_set(
            self: "balethon.Client",
            user_id: int,
            name: str,
            title: str,
            stickers: list
    ):
        data = locals()
        del data["self"]
        return await self.execute("get", "createNewStickerSet", **data)
