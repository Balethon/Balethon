from . import Object
from balethon import objects


class Update(Object):
    attribute_names = [
        ("id", "update_id")
    ]

    def __init__(
            self,
            id: int = None,
            message: "objects.Message" = None,
            edited_message: "objects.EditedMessage" = None,
            channel_post: "objects.Message" = None,
            edited_channel_post: "objects.EditedMessage" = None,
            callback_query: "objects.CallbackQuery" = None,
            shipping_query: "objects.ShippingQuery" = None,
            pre_checkout_query: "objects.PreCheckoutQuery" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.message: "objects.Message" = message
        self.edited_message: "objects.EditedMessage" = edited_message
        self.channel_post: "objects.Message" = channel_post
        self.edited_channel_post: "objects.EditedMessage" = edited_channel_post
        self.callback_query: "objects.CallbackQuery" = callback_query
        self.shipping_query: "objects.ShippingQuery" = shipping_query
        self.pre_checkout_query: "objects.PreCheckoutQuery" = pre_checkout_query

    @property
    def available_update(self):
        for value in self.__dict__.values():
            if isinstance(value, Object):
                return value
