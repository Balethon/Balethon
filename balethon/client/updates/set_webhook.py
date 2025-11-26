import balethon


class SetWebhook:

    async def set_webhook(
            self: "balethon.Client",
            url: str
    ) -> bool:
        return await self.auto_execute("setWebhook", locals())
