from inspect import iscoroutinefunction

from ..smart_call import remove_unwanted_keyword_parameters


class Condition:
    def __init__(self, function=None, can_process=None):
        self.function = function
        self.can_process = can_process

    def is_not_processable(self, event):
        return self.can_process is not None and not isinstance(event, self.can_process)

    async def __call__(self, client, event) -> bool:
        if self.is_not_processable(event):
            return False
        kwargs = dict(condition=self, client=client, event=event)
        kwargs = remove_unwanted_keyword_parameters(self.function, **kwargs)
        if iscoroutinefunction(self.function):
            return await self.function(**kwargs)
        return self.function(**kwargs)

    def __and__(self, other):
        return AllCondition(self, other)

    def __or__(self, other):
        return AnyCondition(self, other)

    def __invert__(self):
        return NotCondition(self)

    def __repr__(self):
        return type(self).__name__


class AllCondition(Condition):
    def __init__(self, *conditions):
        super().__init__()
        self.conditions = conditions

    async def __call__(self, client, event) -> bool:
        for condition in self.conditions:
            if not await condition(client, event):
                return False
        return True

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"All({conditions_string})"


class AnyCondition(Condition):
    def __init__(self, *conditions):
        super().__init__()
        self.conditions = conditions

    async def __call__(self, client, event) -> bool:
        for condition in self.conditions:
            if await condition(client, event):
                return True
        return False

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"Any({conditions_string})"


class NotCondition(Condition):
    def __init__(self, condition):
        super().__init__()
        self.condition = condition

    async def __call__(self, client, event) -> bool:
        return not await self.condition(client, event)

    def __repr__(self):
        return f"Not({self.condition})"


def create(name: str = None, can_process=None):
    def decorator(function):
        CustomCondition = type(name or function.__name__ or "CustomCondition", (Condition,), {})
        return CustomCondition(function, can_process)

    return decorator
