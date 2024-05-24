from typing import Callable
from inspect import iscoroutinefunction
from functools import partial

from ..conditions import Condition
from ..smart_call import remove_unwanted_parameters


class EventHandler:
    can_handle = object

    def __init__(self, callback: Callable, condition=None):
        self.callback = callback
        if not isinstance(condition, Condition) and condition is not None:
            condition = Condition.create(condition)
        self.condition = condition

    async def __call__(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        client = kwargs["client"]
        if event is not None:
            kwargs["event"] = event
        args, kwargs = remove_unwanted_parameters(self.callback, *args, **kwargs)
        if iscoroutinefunction(self.callback):
            return client.dispatcher.event_loop.create_task(self.callback(*args, **kwargs))
        return client.dispatcher.event_loop.run_in_executor(
            client.dispatcher.thread_pool_executor,
            partial(self.callback, *args, **kwargs)
        )

    async def check(self, client, event):
        if self.condition is None:
            return True
        return await self.condition(client, event)
