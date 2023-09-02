class DeleteWebhook:

    async def delete_webhook(self):
        return await self.connection.execute("get", "deleteWebhook")
