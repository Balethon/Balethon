class SetWebhook:

    async def set_webhook(self, url):
        json = {"url": url}
        return await self.connection.execute("post", "setWebhook", json)
