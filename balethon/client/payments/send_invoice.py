import balethon
from ...objects import Message


class SendInvoice:

    async def send_invoice(
            self: "balethon.Client",
            chat_id: int,
            title: str,
            description: str,
            provider_token: str,
            prices
    ):
        json = locals()
        del json["self"]
        result = await self.connection.execute("post", "sendInvoice", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
