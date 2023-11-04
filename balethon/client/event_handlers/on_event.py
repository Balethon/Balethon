import balethon
from ...event_handlers import EventHandler


class OnEvent:

    def on_event(
            self: "balethon.Client",
            condition=None,
            chain="default"
    ):
        return self.add_event_handler(EventHandler, chain, condition)
