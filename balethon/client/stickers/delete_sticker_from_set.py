import balethon


class DeleteStickerFromSet:

    async def delete_sticker_from_set(
            self: "balethon.Client",
            sticker: str
    ) -> bool:
        data = locals()
        del data["self"]
        return await self.execute("get", "deleteStickerToSet", **data)
