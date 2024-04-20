from .condition import Condition


class Equals(Condition):

    def __init__(self, value):
        super().__init__()
        self.value = value

    async def __call__(self, client, event) -> bool:
        from ..objects import Message, CallbackQuery
        if isinstance(event, Message):
            event = event.content
        elif isinstance(event, CallbackQuery):
            event = event.data
        return event == self.value
