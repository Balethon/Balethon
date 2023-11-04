import balethon
from ...event_handlers import ConnectHandler


class OnConnect:

    def on_connect(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(ConnectHandler, chain)
