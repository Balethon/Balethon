import balethon


class DeleteWebhook:

    async def delete_webhook(
            self: "balethon.Client"
    ):
        return await self.execute("get", "deleteWebhook")
