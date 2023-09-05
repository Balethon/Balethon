from . import Object
import balethon
from balethon import objects


class CallbackQuery(Object):
    attribute_names = [
        ("author", "from")
    ]

    def __init__(
            self,
            client: "balethon.Client" = None,
            id: str = None,
            author: "objects.User" = None,
            message: "objects.Message" = None,
            inline_message_id: str = None,
            chat_instance: str = None,
            data: str = None,
            game_short_name: str = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: str = id
        self.author: "objects.User" = author
        self.message: "objects.Message" = message
        self.inline_message_id: str = inline_message_id
        self.chat_instance: str = chat_instance
        self.data: str = data
        self.game_short_name: str = game_short_name

    async def answer(self, text, reply_markup=None, client=None):
        client = client or self.client
        return await client.send_message(self.message.chat.id, text, reply_markup)
