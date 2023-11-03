import balethon


class AddEventHandler:

    def add_event_handler(
            self: "balethon.Client",
            event_handler,
            *args,
            **kwargs
    ):
        if isinstance(event_handler, type):
            def decorator(callback):
                self.add_event_handler(event_handler(callback, *args, **kwargs))
                return callback
            return decorator
        self.dispatcher.add_event_handler(event_handler)
