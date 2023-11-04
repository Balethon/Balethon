import balethon
from ...event_handlers import DisconnectHandler


class OnDisconnect:

    def on_disconnect(
            self: "balethon.Client",
            chain="default"
    ):
        return self.add_event_handler(DisconnectHandler, chain)
