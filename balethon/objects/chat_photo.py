from . import Object


class ChatPhoto(Object):
    attribute_names = [
        ("small_id", "small_file_id"),
        ("small_unique_id", "small_file_unique_id"),
        ("big_id", "big_file_id"),
        ("big_unique_id", "big_file_unique_id")
    ]

    def __init__(
            self,
            small_id: str = None,
            small_unique_id: str = None,
            big_id: str = None,
            big_unique_id: str = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.small_id: str = small_id
        self.small_unique_id: str = small_unique_id
        self.big_id: str = big_id
        self.big_unique_id: str = big_unique_id
