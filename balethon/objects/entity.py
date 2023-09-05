from . import Object
import balethon
from balethon import objects


class Entity(Object):

    def __init__(
            self,
            client: "balethon.Client" = None,
            type: str = None,
            offset: int = None,
            length: int = None,
            url: str = None,
            user: "objects.User" = None,
            **kwargs
    ):
        super().__init__(client, **kwargs)
        self.type: str = type
        self.offset: int = offset
        self.length: int = length
        self.url: str = url
        self.user: "objects.User" = user
