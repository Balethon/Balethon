from . import Object


class Photo(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    def __init__(
            self,
            id: str = None,
            width: int = None,
            height: int = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.size: int = size
