import balethon


class DeleteStickerFromSet:

    async def delete_sticker_from_set(
            self: "balethon.Client",
            name: str
    ):
        data = locals()
        del data["self"]
        return await self.execute("get", "deleteStickerFromSet", **data)
