from .condition import Condition


class IsInstance(Condition):

    def __init__(self, classes):
        super().__init__()
        self.classes = classes

    def __call__(self, client, event) -> bool:
        return isinstance(event, self.classes)
