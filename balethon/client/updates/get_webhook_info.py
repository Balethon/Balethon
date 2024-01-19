import balethon
from ...objects import WebhookInfo


class GetWebhookInfo:

    async def get_webhook_info(
            self: "balethon.Client"
    ) -> WebhookInfo:
        result = await self.execute("post", "getWebhookInfo")
        result = WebhookInfo.wrap(result)
        result.bind(self)
        return result
