import balethon
from ...event_handlers import ErrorHandler


class OnError:

    def on_error(
            self: "balethon.Client",
            condition=None
    ):
        return self.add_event_handler(ErrorHandler, condition)
