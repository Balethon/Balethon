class Condition:

    def __init__(self, function):
        self.function = function

    async def __call__(self, client, update):
        return await self.function(self, client, update)

    def __and__(self, other):
        return AllCondition(self, other)

    def __or__(self, other):
        return AnyCondition(self, other)

    def __invert__(self):
        return NotCondition(self)


class AllCondition(Condition):

    def __init__(self, *conditions):
        super().__init__(None)
        self.conditions = conditions

    async def __call__(self, client, update):
        for condition in self.conditions:
            if not await condition(client, update):
                return False
        return True


class AnyCondition(Condition):

    def __init__(self, *conditions):
        super().__init__(None)
        self.conditions = conditions

    async def __call__(self, client, update):
        for condition in self.conditions:
            if await condition(client, update):
                return True
        return False


class NotCondition(Condition):

    def __init__(self, condition):
        super().__init__(None)
        self.condition = condition

    async def __call__(self, client, update):
        return not await self.condition(client, update)
