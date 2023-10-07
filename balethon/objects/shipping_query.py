from . import Object
from balethon import objects


class ShippingQuery(Object):
    attribute_names = [
        ("author", "from")
    ]

    def __init__(
            self,
            id: str = None,
            author: "objects.User" = None,
            invoice_payload: str = None,
            shipping_address: "objects.ShippingAddress" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.author: "objects.User" = author
        self.invoice_payload: str = invoice_payload
        self.shipping_address: "objects.ShippingAddress" = shipping_address
