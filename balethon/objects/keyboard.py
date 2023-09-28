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
            *rows: List["objects.KeyboardButton"],
            resize: bool = None,
            one_time: bool = None,
            selective: bool = None,
            **kwargs
    ):
        super().__init__(*rows, **kwargs)
        self.resize: bool = resize
        self.one_time: bool = one_time
        self.selective: bool = selective

    def unwrap(self):
        for row in self:
            for button in row:
                button.unwrap()
        super().unwrap()
        self.__dict__["keyboard"] = self
        return self.__dict__
