from . import Object
from balethon import objects


class Sticker(Object):
    attribute_names = [
        ("id", "file_id"),
        ("unique_id", "file_unique_id"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            unique_id: str = None,
            width: int = None,
            height: int = None,
            size: int = None,
            thumb: "objects.Photo" = None,
            emoji: str = None,
            set_name: str = None,
            type: str = None,
            is_animated: bool = None,
            is_video: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.unique_id: str = unique_id
        self.width: int = width
        self.height: int = height
        self.size: int = size
        self.thumb: "objects.Photo" = thumb
        self.emoji: str = emoji
        self.set_name: str = set_name
        self.type: str = type
        self.is_animated: bool = is_animated
        self.is_video: bool = is_video
