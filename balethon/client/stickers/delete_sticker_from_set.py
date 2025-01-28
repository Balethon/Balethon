import balethon


class DeleteStickerFromSet:

    async def delete_sticker_from_set(
            self: "balethon.Client",
            sticker: str
    ) -> bool:
        return await self.auto_execute("get", "deleteStickerToSet", locals())
