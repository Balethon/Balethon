import balethon
from ...objects import Message
from balethon import objects


class SendInvoice:

    async def send_invoice(
            self: "balethon.Client",
            chat_id: int,
            title: str,
            description: str,
            provider_token: str,
            prices,
            provider_data: str = None,
            photo_url: str = None,
            photo_size: int = None,
            photo_width: int = None,
            photo_height: int = None,
            need_name: bool = None,
            need_phone_number: bool = None,
            need_email: bool = None,
            need_shipping_address: bool = None,
            is_flexible: bool = None,
            disable_notification: bool = None,
            reply_to_message_id: int = None,
            reply_markup: "objects.ReplyMarkup" = None
    ):
        json = locals()
        del json["self"]
        result = await self.execute("post", "sendInvoice", json)
        result = Message.wrap(result)
        result.bind(self)
        return result
