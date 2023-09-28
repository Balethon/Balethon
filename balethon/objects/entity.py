from . import Object
from balethon import objects


class Entity(Object):

    def __init__(
            self,
            type: str = None,
            offset: int = None,
            length: int = None,
            url: str = None,
            user: "objects.User" = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.type: str = type
        self.offset: int = offset
        self.length: int = length
        self.url: str = url
        self.user: "objects.User" = user
