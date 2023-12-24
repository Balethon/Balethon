from datetime import datetime

from .event_handler import EventHandler


class DisconnectHandler(EventHandler):

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, client=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        await super().__call__(time=datetime.now(), **kwargs)
