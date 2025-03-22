from typing import Union

from . import Object
from balethon import objects


class InlineKeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            callback_data: str = None,
            url: str = None,
            web_app: Union["objects.WebAppInfo", str] = None,
            copy_text: Union["objects.CopyTextButton", str] = None,
            switch_inline_query: str = None,
            switch_inline_query_current_chat: str = None,
            pay: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.callback_data: str = callback_data
        self.url: str = url
        self.web_app = objects.WebAppInfo(web_app) if isinstance(web_app, str) else web_app
        self.copy_text = objects.CopyTextButton(copy_text) if isinstance(copy_text, str) else copy_text
        self.switch_inline_query: str = switch_inline_query
        self.switch_inline_query_current_chat: str = switch_inline_query_current_chat
        self.pay: bool = pay