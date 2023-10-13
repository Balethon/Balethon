from typing import List

from . import Object
from balethon import objects


class Video(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            thumb: List["objects.Photo"] = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumb: List["objects.Photo"] = thumb
        self.mime_type: str = mime_type
        self.size: int = size
