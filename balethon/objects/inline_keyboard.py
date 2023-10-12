from typing import List
from copy import deepcopy

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
