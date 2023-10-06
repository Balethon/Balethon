from typing import List

from . import ReplyMarkup, InlineKeyboardButton
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    @classmethod
    def wrap(cls, raw_object):
        for i, row in enumerate(raw_object["inline_keyboard"]):
            for j, button in enumerate(row):
                raw_object["inline_keyboard"][i][j] = InlineKeyboardButton.wrap(button)
        return cls(**raw_object)

    def __init__(
            self,
            inline_keyboard: List[List["objects.InlineKeyboardButton"]] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.inline_keyboard: List[List["objects.InlineKeyboardButton"]] = inline_keyboard

    def unwrap(self):
        result = super().unwrap()
        for i, row in enumerate(result["inline_keyboard"]):
            for j, button in enumerate(row):
                result["inline_keyboard"][i][j] = button.unwrap()
        return result
