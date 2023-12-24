from .event_handler import EventHandler


class ErrorHandler(EventHandler):
    can_handle = Exception

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    async def __call__(self, client=None, error=None, *args, **kwargs):
        await super().__call__(*args, client=client, error=error, **kwargs)
