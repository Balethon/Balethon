import balethon
from ...event_handlers import EditedMessageHandler


class OnEditedMessage:

    def on_edited_message(
            self: "balethon.Client",
            condition=None,
            chain="default"
    ):
        return self.add_event_handler(EditedMessageHandler, chain, condition)
