from . import Object
from balethon import objects


class PreCheckoutQuery(Object):
    attribute_names = [("author", "from")]

    def __init__(
        self,
        id: str = None,
        author: "objects.User" = None,
        currency: str = None,
        total_amount: int = None,
        invoice_payload: str = None,
        shipping_option_id: str = None,
        order_info: "objects.OrderInfo" = None,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.author: "objects.User" = author
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.shipping_option_id: str = shipping_option_id
        self.order_info: "objects.OrderInfo" = order_info

    async def answer(self, ok: bool = True, error_message: str = None) -> bool:
        return await self.client.answer_pre_checkout_query(self.id, ok, error_message)

    async def inquire(self) -> "objects.Transaction":
        return await self.client.inquire_transaction(self.id)
