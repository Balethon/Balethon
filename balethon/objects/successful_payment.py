from . import Object
from balethon import objects


class SuccessfulPayment(Object):

    def __init__(
            self,
            currency: str = None,
            total_amount: int = None,
            invoice_payload: str = None,
            shipping_option_id: str = None,
            order_info: "objects.OrderInfo" = None,
            telegram_payment_charge_id: str = None,
            provider_payment_charge_id: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.currency: str = currency
        self.total_amount: int = total_amount
        self.invoice_payload: str = invoice_payload
        self.shipping_option_id: str = shipping_option_id
        self.order_info: "objects.OrderInfo" = order_info
        self.telegram_payment_charge_id: str = telegram_payment_charge_id
        self.provider_payment_charge_id: str = provider_payment_charge_id
