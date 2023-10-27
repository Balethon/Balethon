import balethon


class AddStickerToSet:

    async def add_sticker_to_set(
            self: "balethon.Client",
            user_id: int,
            name: str,
            sticker
    ):
        data = locals()
        del data["self"]
        return await self.execute("get", "addStickerToSet", **data)
