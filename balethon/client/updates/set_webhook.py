class SetWebhook:

    async def set_webhook(self, url):
        json = locals()
        del json["self"]
        return await self.connection.execute("post", "setWebhook", json)
