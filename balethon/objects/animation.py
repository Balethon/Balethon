from . import Object


class Animation(Object):
    attribute_names = [
        ("id", "file_id"),
        ("unique_id", "file_unique_id"),
        ("name", "file_name"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            unique_id: str = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            name: str = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        self.id: str = id
        self.unique_id: str = unique_id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.name: str = name
        self.mime_type: str = mime_type
        self.size: int = size
        super().__init__(**kwargs)
