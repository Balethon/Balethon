import balethon
from ...event_handlers import ShippingQueryHandler


class OnShippingQuery:

    def on_shipping_query(
            self: "balethon.Client",
            condition=None,
            chain="default"
    ):
        return self.add_event_handler(ShippingQueryHandler, chain, condition)
