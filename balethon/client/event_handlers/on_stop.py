import balethon
from ...event_handlers import ShutdownHandler


class OnStop:

    def on_shutdown(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(ShutdownHandler, chain)
