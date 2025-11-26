import balethon
from ...objects import WebhookInfo


class GetWebhookInfo:

    async def get_webhook_info(
            self: "balethon.Client"
    ) -> WebhookInfo:
        return await self.auto_execute("getWebhookInfo", locals())
