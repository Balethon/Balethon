from . import Object
from balethon import objects


class Document(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size"),
        ("name", "file_name")
    ]

    def __init__(
            self,
            id: str = None,
            thumb: "objects.Photo" = None,
            name: str = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.thumb: None = thumb
        self.name: str = name
        self.mime_type: str = mime_type
        self.size: int = size
