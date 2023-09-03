from .. import Object
import balethon


class CallbackQuery(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: str = None,
            author: "balethon.objects.User" = None,
            message: "balethon.objects.Message" = None,
            inline_message_id: str = None,
            chat_instance: str = None,
            data: str = None,
            game_short_name: str = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: str = id
        self.author: "balethon.objects.User" = author
        self.message: "balethon.objects.Message" = message
        self.inline_message_id: str = inline_message_id
        self.chat_instance: str = chat_instance
        self.data: str = data
        self.game_short_name: str = game_short_name

    @classmethod
    def wrap(cls, raw_object):
        if raw_object.get("from"):
            raw_object["author"] = raw_object.pop("from")
        return super().wrap(raw_object)

    async def answer(self, text, reply_markup=None, client=None):
        client = client or self.client
        print(self.message)
        return await client.send_message(self.message.chat.id, text, reply_markup)
