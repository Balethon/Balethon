from .condition import Condition


class Command(Condition):

    def __init__(self, name, arguments=0):
        super().__init__()
        self.name = name
        self.arguments = arguments

    async def __call__(self, client, message) -> bool:
        name, *arguments = message.text.split()
        if name.lower() != f"/{self.name.lower()}":
            return False
        if self.arguments < 0:
            return True
        return self.arguments == len(arguments)
