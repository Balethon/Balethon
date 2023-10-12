from typing import List

from . import ReplyMarkup
from balethon import objects


class Keyboard(ReplyMarkup):
    attribute_names = [
        ("resize", "resize_keyboard"),
        ("one_time", "one_time_keyboard")
    ]

    def __init__(
            self,
            keyboard: List[List["objects.KeyboardButton"]] = None,
            resize: bool = None,
            one_time: bool = None,
            selective: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.keyboard: List[List["objects.KeyboardButton"]] = keyboard
        self.resize: bool = resize
        self.one_time: bool = one_time
        self.selective: bool = selective
