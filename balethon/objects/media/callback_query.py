from ..object import Object
from .. import User
from .message import Message


class CallbackQuery(Object):
    id: int
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
