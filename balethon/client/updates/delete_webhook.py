import balethon


class DeleteWebhook:

    async def delete_webhook(
            self: "balethon.Client"
    ) -> bool:
        return await self.auto_execute("deleteWebhook", locals())
