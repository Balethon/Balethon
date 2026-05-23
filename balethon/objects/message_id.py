from typing import Union

from . import Object


class MessageId(Object):
    def __init__(
            self,
            message_id: Union[str, tuple] = None,
            *,
            rid: int = None,
            date: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        if message_id is not None and isinstance(message_id, str):
            rid, date = map(int, message_id.split(":"))
        elif message_id is not None:
            rid, date = message_id
        self.rid = rid
        self.date = date

    def __str__(self):
        return f"{self.rid}:{self.date}"


def resolve_message_id(message_id: Union[str, tuple, MessageId]) -> MessageId:
    if not isinstance(message_id, MessageId):
        message_id = MessageId(message_id)

    return message_id
