from inspect import iscoroutinefunction


class EventHandler:
    can_handle = object

    def __init__(self, callback, condition=None):
        self.callback = callback
        self.condition = condition

    async def __call__(self, *args, **kwargs):
        if iscoroutinefunction(self.callback):
            return await self.callback(*args, **kwargs)
        return self.callback(*args, **kwargs)

    async def check(self, client, update):
        if self.condition is None:
            return True
        return await self.condition(client, update)
