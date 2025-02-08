from datetime import datetime

from .event_handler import EventHandler


class InitializeHandler(EventHandler):

    @property
    def can_handle(self):
        return InitializeHandler

    def __init__(self, callback):
        super().__init__(callback)

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        await super().handle(*args, **kwargs, time=datetime.now())
