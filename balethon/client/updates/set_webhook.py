import balethon


class SetWebhook:

    async def set_webhook(
            self: "balethon.Client",
            url: str
    ):
        json = locals()
        del json["self"]
        return await self.execute("post", "setWebhook", json)
