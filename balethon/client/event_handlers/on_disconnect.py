import balethon
from ...event_handlers import DisconnectHandler


class OnDisconnect:

    def on_connect(
            self: "balethon.Client"
    ):
        return self.add_event_handler(DisconnectHandler)
