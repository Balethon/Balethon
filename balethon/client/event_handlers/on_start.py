import balethon
from ...event_handlers import StartHandler


class OnStart:

    def on_start(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(StartHandler, chain)
