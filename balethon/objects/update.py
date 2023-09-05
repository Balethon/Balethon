from . import Object
import balethon
from balethon import objects


class Update(Object):
    attribute_names = [
        ("id", "update_id")
    ]

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: int = None,
            message: "objects.Message" = None,
            edited_message: "objects.Message" = None,
            channel_post: "objects.Message" = None,
            edited_channel_post: "objects.Message" = None,
            callback_query: "objects.CallbackQuery" = None,
            shipping_query: None = None,
            pre_checkout_query: None = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: int = id
        self.message: "objects.Message" = message
        self.edited_message: "objects.Message" = edited_message
        self.channel_post: "objects.Message" = channel_post
        self.edited_channel_post: "objects.Message" = edited_channel_post
        self.callback_query: "objects.CallbackQuery" = callback_query
        self.shipping_query: None = shipping_query
        self.pre_checkout_query: None = pre_checkout_query

    @property
    def available_update(self):
        for value in self.__dict__.values():
            if isinstance(value, Object):
                return value
