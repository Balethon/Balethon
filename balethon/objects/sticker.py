from . import Object
from balethon import objects


class Sticker(Object):

    def __init__(
            self,
            file_id: str = None,
            file_unique_id: str = None,
            width: int = None,
            height: int = None,
            thumb: "objects.Photo" = None,
            emoji: str = None,
            set_name: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.file_id: str = file_id
        self.file_unique_id: str = file_unique_id
        self.width: int = width
        self.height: int = height
        self.thumb: "objects.Photo" = thumb
        self.emoji: str = emoji
        self.set_name: str = set_name
