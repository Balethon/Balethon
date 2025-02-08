from .event_handler import EventHandler
from ..objects import Object


class UpdateHandler(EventHandler):
    can_handle = Object

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    async def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["update"] = event
        await super().handle(*args, **kwargs)
