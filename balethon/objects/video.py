from . import Object


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
            thumb: None = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumb: None = thumb
        self.mime_type: str = mime_type
        self.size: int = size
