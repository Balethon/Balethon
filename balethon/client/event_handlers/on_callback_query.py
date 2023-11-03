import balethon
from ...event_handlers import CallbackQueryHandler


class OnCallbackQuery:

    def on_callback_query(
            self: "balethon.Client",
            condition=None
    ):
        return self.add_event_handler(CallbackQueryHandler, condition)
