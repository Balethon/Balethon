from . import Object


class Audio(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            duration: int = None,
            performer: str = None,
            title: str = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.duration: int = duration
        self.performer: str = performer
        self.title: str = title
        self.mime_type: str = mime_type
        self.size: int = size
