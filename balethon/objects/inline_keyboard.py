from typing import List

from . import ReplyMarkup
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    def __init__(
            self,
            *rows: List["objects.InlineKeyboardButton"],
            **kwargs
    ):
        super().__init__(*rows, **kwargs)

    def unwrap(self):
        super().unwrap()
        for row in self:
            print(row)
            for i, button in enumerate(row):
                print(button)
                self = button.unwrap()
                print(button.__dict__)
        return {"inline_keyboard": list(self)}
