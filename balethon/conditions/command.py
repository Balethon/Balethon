from .condition import Condition
from ..objects import Message


class Command(Condition):
    def __init__(self, name, prefix="/", min_arguments=None, max_arguments=None):
        super().__init__(can_process=Message)
        self.name = name
        self.prefix = prefix
        self.min_arguments = min_arguments
        self.max_arguments = max_arguments

    async def __call__(self, client, event) -> bool:
        if not event.text:
            return False
        name, *arguments = event.text.split()
        if name.lower() != f"{self.prefix}{self.name.lower()}":
            return False
        if self.min_arguments is not None and len(arguments) < self.min_arguments:
            return False
        if self.max_arguments is not None and len(arguments) > self.max_arguments:
            return False
        return True
