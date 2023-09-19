from .condition import Condition


class Command(Condition):

    def __init__(self, name):
        super().__init__()
        self.name = name

    async def __call__(self, client, message):
        if not message.text.startswith("/"):
            return False
        if not message.text[1:].startswith(self.name):
            return False
        return True
