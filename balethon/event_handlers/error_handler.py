from .event_handler import EventHandler


class ErrorHandler(EventHandler):
    can_handle = Exception

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["error"] = event
        await super().handle(*args, **kwargs)
