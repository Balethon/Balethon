import balethon
from ...event_handlers import StopHandler


class OnStop:

    def on_stop(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(StopHandler, chain)
