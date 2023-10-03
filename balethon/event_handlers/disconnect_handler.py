from .event_handler import EventHandler


class DisconnectHandler(EventHandler):

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, client, *args, **kwargs):
        await super().__call__(client)

    async def check(self, client, update):
        try:
            return isinstance(self, update)
        except TypeError:
            return False
