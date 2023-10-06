from . import Object


class InlineKeyboardButton(Object):

    def __init__(
            self,
            text: str = None,
            callback_data: str = None,
            url: str = None,
            switch_inline_query: str = None,
            switch_inline_query_current_chat: str = None,
            pay: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.text: str = text
        self.callback_data: str = callback_data
        self.url: str = url
        self.switch_inline_query: str = switch_inline_query
        self.switch_inline_query_current_chat: str = switch_inline_query_current_chat
        self.pay: bool = pay
