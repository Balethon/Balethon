import balethon


class RemoveEventHandler:

    def remove_event_handler(
            self: "balethon.Client",
            event_handler
    ):
        self.dispatcher.remove_event_handler(event_handler)
