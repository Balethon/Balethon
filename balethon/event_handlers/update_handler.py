from .event_handler import EventHandler
from ..objects import Object


class UpdateHandler(EventHandler):
    can_handle = Object

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    async def __call__(self, client=None, update=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if update is not None:
            kwargs["update"] = update
        await super().__call__(*args, **kwargs)
