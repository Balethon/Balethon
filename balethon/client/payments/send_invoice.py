from ...objects import Message


class SendInvoice:

    async def send_invoice(self, chat_id, title, description, provider_token, prices):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendInvoice", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
