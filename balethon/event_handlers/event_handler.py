from inspect import iscoroutinefunction


class EventHandler:
    can_handle = object

    def __init__(self, callback, condition=None):
        self.callback = callback
        self.condition = condition

    async def __call__(self, client, *args, **kwargs):
        if iscoroutinefunction(self.callback):
            return await self.callback(client, *args, **kwargs)
        return client.dispatcher.event_loop.run_in_executor(
            client.dispatcher.thread_pool_executor,
            self.callback,
            client,
            *args,
            **kwargs
        )

    async def check(self, client, update):
        if self.condition is None:
            return True
        return await self.condition(client, update)
