import balethon
from ...event_handlers import EventHandler


class OnEvent:

    def on_event(
            self: "balethon.Client",
            condition=None
    ):
        return self.add_event_handler(EventHandler, condition)
