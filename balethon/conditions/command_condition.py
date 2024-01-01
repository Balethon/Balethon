from .condition import Condition


class Command(Condition):

    def __init__(self, name, min_arguments=None, max_arguments=None):
        super().__init__()
        self.name = name
        self.min_arguments = min_arguments
        self.max_arguments = max_arguments

    async def __call__(self, client, message) -> bool:
        name, *arguments = message.text.split()
        if name.lower() != f"/{self.name.lower()}":
            return False
        if self.min_arguments is not None and len(arguments) < self.min_arguments:
            return False
        if self.max_arguments is not None and len(arguments) > self.max_arguments:
            return False
        return True
