from ..object import Object


class Thumb(Object):

    def __init__(
            self,
            file_id=None,
            width=None,
            height=None,
            file_size=None,
            **kwargs
    ):
        super().__init__()
        self.file_id = file_id
        self.width = width
        self.height = height
        self.file_size = file_size
