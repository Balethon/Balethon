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
            edited_message: "objects.Message" = None,
            channel_post: "objects.Message" = None,
            edited_channel_post: "objects.Message" = None,
            callback_query: "objects.CallbackQuery" = None,
            shipping_query: "objects.ShippingQuery" = None,
            pre_checkout_query: "objects.PreCheckoutQuery" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.message: "objects.Message" = message
        self.edited_message: "objects.Message" = edited_message
        self.channel_post: "objects.Message" = channel_post
        self.edited_channel_post: "objects.Message" = edited_channel_post
        self.callback_query: "objects.CallbackQuery" = callback_query
        self.shipping_query: "objects.ShippingQuery" = shipping_query
        self.pre_checkout_query: "objects.PreCheckoutQuery" = pre_checkout_query

    @property
    def available_update(self):
        for value in self.__dict__.values():
            if isinstance(value, Object):
                return value

    @property
    def available_update_event_handler_type(self):
        from ..event_handlers import (
            MessageHandler,
            EditedMessageHandler,
            CallbackQueryHandler,
            ShippingQueryHandler,
            PreCheckoutQueryHandler
        )
        for name, value in self.__dict__.items():
            if not isinstance(value, Object):
                continue
            if name in ("message", "channel_post"):
                return MessageHandler
            elif name in ("edited_message", "edited_channel_post"):
                return EditedMessageHandler
            elif name == "callback_query":
                return CallbackQueryHandler
            elif name == "shipping_query":
                return ShippingQueryHandler
            elif name == "pre_checkout_query":
                return PreCheckoutQueryHandler
