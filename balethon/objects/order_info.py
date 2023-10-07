from . import Object
from balethon import objects


class OrderInfo(Object):

    def __init__(
            self,
            name: str = None,
            phone_number: str = None,
            email: str = None,
            shipping_address: "objects.ShippingAddress" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.name: str = name
        self.phone_number: str = phone_number
        self.email: str = email
        self.shipping_address: "objects.ShippingAddress" = shipping_address
