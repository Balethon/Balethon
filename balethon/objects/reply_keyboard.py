from typing import Union, List

from . import ReplyMarkup, ReplyKeyboardButton
from .list import List as BalethonList
from balethon import objects


class ReplyKeyboard(ReplyMarkup):
    attribute_names = [
        ("resize", "resize_keyboard"),
        ("one_time", "one_time_keyboard")
    ]

    def __init__(
            self,
            *rows: List[Union["objects.ReplyKeyboardButton", str]],
            resize: bool = None,
            one_time: bool = None,
            selective: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.keyboard: List[List["objects.ReplyKeyboardButton"]] = BalethonList()
        for row in rows:
            self.add_row(*row)
        self.resize: bool = resize
        self.one_time: bool = one_time
        self.selective: bool = selective

    def add_button(self, button: Union["objects.ReplyKeyboardButton", str], row_index: int = -1, button_index: int = -1):
        if isinstance(button, str):
            button = ReplyKeyboardButton(button)
        if button_index == -1:
            self.keyboard[row_index].append(button)
        elif button_index < 0:
            self.keyboard[row_index].insert(button_index + 1, button)
        else:
            self.keyboard[row_index].insert(button_index, button)

    def add_row(self, *row: Union["objects.ReplyKeyboardButton", str], row_index: int = -1):
        if row_index == -1:
            self.keyboard.append(BalethonList())
        elif row_index < 0:
            self.keyboard.insert(row_index + 1, BalethonList())
        else:
            self.keyboard.insert(row_index, BalethonList())
        for button in row:
            self.add_button(button, row_index)
