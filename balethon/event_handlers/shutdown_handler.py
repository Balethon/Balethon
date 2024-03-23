from datetime import datetime

from .event_handler import EventHandler


class ShutdownHandler(EventHandler):

    @property
    def can_handle(self):
        return ShutdownHandler

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        await super().__call__(*args, **kwargs, time=datetime.now())
