class SendInvoice:

    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = {"chat_id": chat_id, "title": title, "description": description, "provider_token": provider_token, "prices": prices}
        return await self.connection.execute("post", "sendInvoice", json)