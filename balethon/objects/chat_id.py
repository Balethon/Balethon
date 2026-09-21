from typing import Union

from . import Object
from ..enums import ChatType


class ChatId(Object):
    def __init__(
            self,
            chat_id: Union[int, str, tuple] = None,
            *,
            peer_id: Union[int, str] = None,
            peer_type: Union[int, str, ChatType] = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        if chat_id is not None and isinstance(chat_id, str) and ":" in chat_id:
            peer_id, peer_type = chat_id.split(":")
        elif chat_id is not None and isinstance(chat_id, (int, str)):
            peer_id = chat_id
        elif chat_id is not None:
            peer_id, peer_type = chat_id
        if isinstance(peer_type, ChatType):
            peer_type = peer_type.to_protobuf()
        if peer_type is not None:
            peer_type = int(peer_type)
        self.peer_id = int(peer_id)
        self.peer_type = peer_type

    def __str__(self):
        if self.peer_type is None:
            return str(self.peer_id)
        return f"{self.peer_id}:{self.peer_type}"
