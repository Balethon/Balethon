from re import compile

from .condition import Condition
from ..objects import Message, CallbackQuery


class Regex(Condition):
    def __init__(self, pattern, flags=0):
        super().__init__(can_process=(Message, CallbackQuery))
        self.pattern = compile(pattern, flags)

    async def __call__(self, client, event) -> bool:
        if isinstance(event, Message):
            event = event.content
        elif isinstance(event, CallbackQuery):
            event = event.data
        return bool(list(self.pattern.finditer(event)) or None)
