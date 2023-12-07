from typing import Union, List, Tuple

from . import ReplyMarkup, InlineKeyboardButton
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    def __init__(
            self,
            *rows: List[Union["objects.InlineKeyboardButton", Tuple[str, str]]],
            **kwargs
    ):
        super().__init__(**kwargs)
        self.inline_keyboard: List[List["objects.InlineKeyboardButton"]] = []
        for row in rows:
            self.add_row(*row)

    def add_button(self, button: Union["objects.InlineKeyboardButton", Tuple[str, str]], row_index: int = -1, button_index: int = -1):
        if isinstance(button, tuple):
            button = InlineKeyboardButton(*button)
        if button_index == -1:
            self.inline_keyboard[row_index].append(button)
        elif button_index < 0:
            self.inline_keyboard[row_index].insert(button_index + 1, button)
        else:
            self.inline_keyboard[row_index].insert(button_index, button)

    def add_row(self, *row: Union["objects.InlineKeyboardButton", Tuple[str, str]], row_index: int = -1):
        if row_index == -1:
            self.inline_keyboard.append([])
        elif row_index < 0:
            self.inline_keyboard.insert(row_index + 1, [])
        else:
            self.inline_keyboard.insert(row_index, [])
        for button in row:
            self.add_button(button, row_index)
