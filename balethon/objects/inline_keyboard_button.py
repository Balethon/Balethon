from . import Object
import balethon


class InlineKeyboardButton(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            text: str = None,
            url: str = None,
            callback_data: str = None,
            switch_inline_query: str = None,
            switch_inline_query_current_chat: str = None,
            pay: bool = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.text: str = text
        self.url: str = url
        self.callback_data: str = callback_data
        self.switch_inline_query: str = switch_inline_query
        self.switch_inline_query_current_chat: str = switch_inline_query_current_chat
        self.pay: bool = pay