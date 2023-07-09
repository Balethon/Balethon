class Condition:

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return await self.function(*args, **kwargs)

    def __repr__(self):
        return ""

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    def __invert__(self):
        pass
