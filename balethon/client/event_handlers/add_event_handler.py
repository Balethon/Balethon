import balethon


class AddEventHandler:

    def add_event_handler(
            self: "balethon.Client",
            event_handler,
            chain="default",
            *args,
            **kwargs
    ):
        if isinstance(event_handler, type):
            def decorator(callback):
                self.add_event_handler(event_handler(callback, *args, **kwargs), chain)
                return callback
            return decorator
        self.dispatcher.add_event_handler(event_handler, chain)
