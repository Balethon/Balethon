class EventHandler:
    can_handle = object

    def __init__(self, callback):
        self.callback = callback

    async def __call__(self, *args, **kwargs):
        return await self.callback(*args, **kwargs)
