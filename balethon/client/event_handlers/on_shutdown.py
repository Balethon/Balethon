import balethon
from ...event_handlers import ShutdownHandler


class OnShutdown:

    def on_shutdown(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(ShutdownHandler, chain)
