from .event_handler import EventHandler


class DisconnectHandler(EventHandler):

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, client, *args, **kwargs):
        await super().__call__(client)
