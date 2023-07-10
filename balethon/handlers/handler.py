class Handler:

    def __init__(self, callback, condition=None):
        self.callback = callback
        self.condition = condition

    async def check(self, client, update):
        if callable(self.condition):
            return await self.condition(client, update)
        return True
