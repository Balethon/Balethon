from typing import Union, List

import balethon
from ...objects import Message, LabeledPrice
from balethon import objects


class SendInvoice:

    async def send_invoice(
            self: "balethon.Client",
            chat_id: Union[int, str],
            title: str,
            description: str,
            payload: str,
            provider_token: str,
            prices: List[LabeledPrice],
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
    ) -> Message:
        chat_id = await self.resolve_peer_id(chat_id)
        data = locals()
        for i, price in enumerate(prices):
            if isinstance(price, LabeledPrice):
                prices[i] = price.unwrap()
        del data["self"]
        result = await self.execute("post", "sendInvoice", **data)
        result = Message.wrap(result)
        result.bind(self)
        return result
