from typing import Callable
from inspect import iscoroutinefunction
from functools import partial

from ..conditions import Condition, create
from ..smart_call import remove_unwanted_parameters


class EventHandler:
    can_handle = object

    def __init__(self, callback: Callable, condition=None):
        self.callback = callback
        if not isinstance(condition, Condition) and condition is not None:
            condition = create(condition)
        self.condition = condition
        self.self = None

    def to_string(self, keyword="if", tabs=0):
        result = []
        condition = self.condition or self.can_handle.__name__
        result.append(f"{keyword} {condition}:")
        result.append(f"    {type(self).__name__}({self.can_handle.__name__})")
        return "\n".join(f"{'    ' * tabs}{i}" for i in result)

    def __repr__(self):
        return self.to_string()

    async def __call__(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        client = kwargs["client"]
        if self.self is not None:
            args = list(args)
            args.insert(0, self.self)
        if event is not None:
            kwargs["event"] = event
        args, kwargs = remove_unwanted_parameters(self.callback, *args, **kwargs)
        if iscoroutinefunction(self.callback):
            return await self.callback(*args, **kwargs)
        return client.dispatcher.event_loop.run_in_executor(
            client.dispatcher.sync_workers,
            partial(self.callback, *args, **kwargs)
        )

    async def check(self, client, event):
        if self.condition is None:
            return True
        return await self.condition(client, event)
