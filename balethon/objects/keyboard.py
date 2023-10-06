from typing import List

from . import ReplyMarkup, KeyboardButton
from balethon import objects


class Keyboard(ReplyMarkup):
    attribute_names = [
        ("resize", "resize_keyboard"),
        ("one_time", "one_time_keyboard")
    ]

    @classmethod
    def wrap(cls, raw_object):
        for i, row in enumerate(raw_object["keyboard"]):
            for j, button in enumerate(row):
                raw_object["keyboard"][i][j] = KeyboardButton.wrap(button)
        return cls(**raw_object)

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

    def unwrap(self):
        result = super().unwrap()
        for i, row in enumerate(result["keyboard"]):
            for j, button in enumerate(row):
                result["keyboard"][i][j] = button.unwrap()
        return result
