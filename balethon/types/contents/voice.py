from ..object import Object


class Voice(Object):

    def __init__(
            self,
            file_id=None,
            duration=None,
            mime_type=None,
            file_size=None,
            **kwargs
    ):
        super().__init__()
        self.file_id = file_id
        self.duration = duration
        self.mime_type = mime_type
        self.file_size = file_size
