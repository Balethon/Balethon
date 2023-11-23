import balethon


class DeleteWebhook:

    async def delete_webhook(
            self: "balethon.Client"
    ) -> bool:
        return await self.execute("get", "deleteWebhook")
