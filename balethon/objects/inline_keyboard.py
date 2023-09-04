from typing import List

from . import Object
import balethon
from balethon import objects


class InlineKeyboard(Object, list):

    def __init__(
            self,
            client: "balethon.Client" = None,
            *rows: List["objects.InlineKeyboardButton"],
            **kwargs
    ):
        super().__init__(client, **kwargs)
        list.__init__(self, rows)

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(i) for i in self)})"
