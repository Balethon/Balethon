from . import Object


class Document(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            thumb: None = None,
            file_name: str = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.thumb: None = thumb
        self.file_name: str = file_name
        self.mime_type: str = mime_type
        self.size: int = size
