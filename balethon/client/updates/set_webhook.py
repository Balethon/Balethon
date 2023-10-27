import balethon


class SetWebhook:

    async def set_webhook(
            self: "balethon.Client",
            url: str
    ):
        data = locals()
        del data["self"]
        return await self.execute("post", "setWebhook", **data)
