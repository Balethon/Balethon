from typing import Union, List, Tuple

from . import ReplyMarkup, InlineKeyboardButton
from .list import List as BalethonList
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    def __init__(
            self,
            *rows: List[Union["objects.InlineKeyboardButton", Tuple[str, str]]],
            **kwargs
    ):
        super().__init__(**kwargs)
        self.inline_keyboard: List[List["objects.InlineKeyboardButton"]] = BalethonList()
        for row in rows:
            self.add_row(*row)

    def add_button(
            self,
            button: Union["objects.InlineKeyboardButton", Tuple[str, str]],
            row_index: int = -1,
            button_index: int = -1
    ):
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
            self.inline_keyboard.append(BalethonList())
        elif row_index < 0:
            self.inline_keyboard.insert(row_index + 1, BalethonList())
        else:
            self.inline_keyboard.insert(row_index, BalethonList())
        for button in row:
            self.add_button(button, row_index)

    def on_click(self, row_index: int, button_index: int):
        from ..conditions import click
        return click(self, row_index, button_index)
