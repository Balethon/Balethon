from typing import List

from . import ReplyMarkup
import balethon
from balethon import objects


class Keyboard(ReplyMarkup):

    def __init__(
            self,
            client: "balethon.Client" = None,
            *rows: List["objects.KeyboardButton"],
            resize: bool = None,
            one_time: bool = None,
            selective: bool = None,
            **kwargs
    ):
        super().__init__(client, *rows, **kwargs)
        self.resize: bool = resize
        self.one_time: bool = one_time
        self.selective: bool = selective
