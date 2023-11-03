import balethon
from ...event_handlers import MessageHandler


class OnMessage:

    def on_message(
            self: "balethon.Client",
            condition=None
    ):
        return self.add_event_handler(MessageHandler, condition)
