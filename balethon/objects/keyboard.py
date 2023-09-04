from typing import List

from . import Object
import balethon
from balethon import objects


class Keyboard(Object, list):

    def __init__(
            self,
            client: "balethon.Client" = None,
            *rows: List["objects.KeyboardButton"],
            resize: bool = None,
            one_time: bool = None,
            selective: bool = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        list.__init__(self, rows)
        self.resize: bool = resize
        self.one_time: bool = one_time
        self.selective: bool = selective

    def __repr__(self):
        return f"{type(self).__name__}({', '.join(repr(i) for i in self)})"
