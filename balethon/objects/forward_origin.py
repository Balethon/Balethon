from balethon import enums
from . import Object
from .. import objects


class ForwardOrigin(Object):

    def __init__(
            self,
            type: "enums.PeerType" = None,
            date: "objects.Date" = None,
            sender_user: "objects.User" = None,
            chat: "objects.Chat" = None,
            message_id: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: "enums.PeerType" = type
        self.date: "objects.Date" = date
        self.sender_user: "objects.User" = sender_user
        self.chat: "objects.Chat" = chat
        self.message_id: int = message_id
