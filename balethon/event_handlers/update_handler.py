from .event_handler import EventHandler
from ..objects import Object


class UpdateHandler(EventHandler):
    can_handle = Object

    def __init__(self, callback, condition=None):
        super().__init__(callback)
        self.condition = condition

    async def check(self, client, update):
        if callable(self.condition):
            return await self.condition(client, update)
        return True
