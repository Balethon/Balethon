from datetime import datetime

from .event_handler import EventHandler


class ConnectHandler(EventHandler):

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, client=None, *args, **kwargs):
        await super().__call__(client=client, time=datetime.now(), **kwargs)
