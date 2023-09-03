from . import Object
import balethon


class Update(Object):

    @classmethod
    def wrap(cls, raw_object):
        if raw_object.get("update_id"):
            raw_object["id"] = raw_object.pop("update_id")
        return super().wrap(raw_object)

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: int = None,
            message: "balethon.objects.Message" = None,
            edited_message: "balethon.objects.Message" = None,
            channel_post: "balethon.objects.Message" = None,
            edited_channel_post: "balethon.objects.Message" = None,
            callback_query: "balethon.objects.CallbackQuery" = None,
            shipping_query: None = None,
            pre_checkout_query: None = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: int = id
        self.message: "balethon.objects.Message" = message
        self.edited_message: "balethon.objects.Message" = edited_message
        self.channel_post: "balethon.objects.Message" = channel_post
        self.edited_channel_post: "balethon.objects.Message" = edited_channel_post
        self.callback_query: "balethon.objects.CallbackQuery" = callback_query
        self.shipping_query: None = shipping_query
        self.pre_checkout_query: None = pre_checkout_query

    def get_update(self):
        for value in self.__dict__.values():
            if isinstance(value, Object):
                return value
