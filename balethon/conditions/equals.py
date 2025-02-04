from .condition import Condition
from ..objects import Message, CallbackQuery


class Equals(Condition):
    def __init__(self, *values):
        super().__init__(can_process=(Message, CallbackQuery))
        self.values = values

    async def __call__(self, client, event) -> bool:
        if isinstance(event, Message):
            return event.content in self.values
        elif isinstance(event, CallbackQuery):
            return event.data in self.values
