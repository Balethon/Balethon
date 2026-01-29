from .condition import Condition


class IsInstance(Condition):
    def __init__(self, classes):
        super().__init__()
        self.classes = classes

    async def __call__(self, client, event) -> bool:
        if self.is_not_processable(event):
            return False
        return isinstance(event, self.classes)
