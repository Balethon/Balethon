from typing import List

from . import ReplyMarkup
import balethon
from balethon import objects


class InlineKeyboard(ReplyMarkup):

    def __init__(
            self,
            client: "balethon.Client" = None,
            *rows: List["objects.InlineKeyboardButton"],
            **kwargs
    ):
        super().__init__(client, *rows, **kwargs)
