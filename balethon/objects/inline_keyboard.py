from typing import List

from . import ReplyMarkup
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    def __init__(
            self,
            inline_keyboard: List[List["objects.InlineKeyboardButton"]] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.inline_keyboard: List[List["objects.InlineKeyboardButton"]] = inline_keyboard
