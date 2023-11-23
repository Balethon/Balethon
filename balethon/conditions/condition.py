from inspect import iscoroutinefunction


class Condition:

    @classmethod
    def create(cls, function):
        return type(function.__name__ or "CustomCondition", (cls,), {})(function)

    def __init__(self, function=None):
        self.function = function

    async def __call__(self, client, update) -> bool:
        if iscoroutinefunction(self.function):
            return await self.function(self, client, update)
        return self.function(self, client, update)

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

    async def __call__(self, client, update) -> bool:
        for condition in self.conditions:
            if not await condition(client, update):
                return False
        return True

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"All({conditions_string})"


class AnyCondition(Condition):

    def __init__(self, *conditions):
        super().__init__()
        self.conditions = conditions

    async def __call__(self, client, update) -> bool:
        for condition in self.conditions:
            if await condition(client, update):
                return True
        return False

    def __repr__(self):
        conditions_string = ", ".join(map(str, self.conditions))
        return f"Any({conditions_string})"


class NotCondition(Condition):

    def __init__(self, condition):
        super().__init__()
        self.condition = condition

    async def __call__(self, client, update) -> bool:
        return not await self.condition(client, update)

    def __repr__(self):
        return f"Not({self.condition})"
