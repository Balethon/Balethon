import balethon
from ...event_handlers import InitializeHandler


class OnInitialize:

    def on_initialize(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(InitializeHandler, chain)
