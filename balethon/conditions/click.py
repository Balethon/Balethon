import re

from .condition import Condition
from ..objects import Message, CallbackQuery, ReplyKeyboard, InlineKeyboard


class Click(Condition):
    def __init__(self, keyboard, row_index: int, button_index: int):
        super().__init__(can_process=(Message, CallbackQuery))
        self.keyboard = keyboard
        self.row_index = row_index
        self.button_index = button_index

    @staticmethod
    def create_regex(text):
        return "^" + re.sub(r"{.*?}", ".*", text) + "$"

    async def process(self, client, event) -> bool:
        if isinstance(self.keyboard, ReplyKeyboard) and isinstance(event, Message):
            button = self.keyboard.keyboard[self.row_index][self.button_index]
            return bool(re.match(self.create_regex(button.text), event.text))
        elif isinstance(self.keyboard, InlineKeyboard) and isinstance(event, CallbackQuery):
            button = self.keyboard.inline_keyboard[self.row_index][self.button_index]
            return bool(re.match(self.create_regex(button.callback_data), event.data))
