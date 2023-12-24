from .event_handler import EventHandler


class ErrorHandler(EventHandler):
    can_handle = Exception

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    async def __call__(self, client=None, error=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if error is not None:
            kwargs["error"] = error
        await super().__call__(*args, **kwargs)
