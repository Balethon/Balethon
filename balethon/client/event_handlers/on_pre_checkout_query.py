import balethon
from ...event_handlers import PreCheckoutQueryHandler


class OnPreCheckoutQuery:

    def on_pre_checkout_query(
            self: "balethon.Client",
            condition=None,
            chain="default"
    ):
        return self.add_event_handler(PreCheckoutQueryHandler, chain, condition)
