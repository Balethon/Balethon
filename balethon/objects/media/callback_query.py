from .. import Object
from .. import User
from . import Message


class CallbackQuery(Object):

    def __init__(
            self,
            client=None,
            id: str = None,
            author: User = None,
            message: Message = None,
            inline_message_id: str = None,
            chat_instance: str = None,
            data: str = None,
            game_short_name: str = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.id: str = id
        self.author: User = author
        self.message: Message = message
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
