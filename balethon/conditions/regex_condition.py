from re import compile

from .condition import Condition


class Regex(Condition):

    def __init__(self, pattern, flags=0):
        super().__init__()
        self.pattern = compile(pattern, flags)

    async def __call__(self, client, update):
        from ..objects import Message, CallbackQuery
        if isinstance(update, Message):
            update = update.text or update.caption
        elif isinstance(update, CallbackQuery):
            update = update.data
        return bool(list(self.pattern.finditer(update)) or None)
