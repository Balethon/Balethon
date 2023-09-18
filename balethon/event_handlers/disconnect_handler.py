from .event_handler import EventHandler


class DisconnectHandler(EventHandler):

    @property
    def can_handle(self):
        return type(self)

    def __init__(self, callback):
        super().__init__(callback)

    async def __call__(self, client, *args, **kwargs):
        await super().__call__(client)
