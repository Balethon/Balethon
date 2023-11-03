import balethon
from ...event_handlers import CommandHandler


class OnCommand:

    def on_command(
            self: "balethon.Client",
            condition=None,
            name=None
    ):
        return self.add_event_handler(CommandHandler, condition, name)
