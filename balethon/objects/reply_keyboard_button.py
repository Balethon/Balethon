from typing import Union
from copy import deepcopy

from . import Object
from balethon import enums, objects


class ReplyKeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            request_contact: bool = None,
            request_location: bool = None,
            web_app: Union["objects.WebAppInfo", str] = None,
            style: "enums.ButtonStyle" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.request_contact: bool = request_contact
        self.request_location: bool = request_location
        self.web_app = objects.WebAppInfo(web_app) if isinstance(web_app, str) else web_app
        self.style: "enums.ButtonStyle" = style

    def format(self, *args, **kwargs):
        button = deepcopy(self)
        if button.text:
            button.text = button.text.format(*args, **kwargs)
        if button.web_app:
            button.web_app = button.web_app.format(*args, **kwargs)
        return button
