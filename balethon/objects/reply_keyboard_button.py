from typing import Union

from . import Object
from balethon import objects


class ReplyKeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            request_contact: bool = None,
            request_location: bool = None,
            web_app: Union["objects.WebAppInfo", str] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.request_contact: bool = request_contact
        self.request_location: bool = request_location
        self.web_app = objects.WebAppInfo(web_app) if isinstance(web_app, str) else web_app
