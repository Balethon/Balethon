from . import Object


class File(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size"),
        ("path", "file_path")
    ]

    def __init__(
            self,
            id: str = None,
            size: int = None,
            path: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.size: int = size
        self.path: str = path
