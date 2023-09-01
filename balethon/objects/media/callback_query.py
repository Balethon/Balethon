from .. import Object
from .. import User
from . import Message


class CallbackQuery(Object):
    id: str
    author: User
    message: Message
    inline_message_id: str
    chat_instance: str
    data: str
    game_short_name: str

    def __init__(self, **kwargs):
        if kwargs.get("from"):
            kwargs["author"] = kwargs.pop("from")
        super().__init__(**kwargs)

    async def answer(self, text, reply_markup=None, client=None):
        client = client or self.client
        return await client.send_message(self.message.chat.id, text, reply_markup)
