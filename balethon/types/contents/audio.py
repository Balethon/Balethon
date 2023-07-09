from ..object import Object


class Audio(Object):
    def __init__(
            self,
            file_id=None,
            duration=None,
            performer=None,
            title=None,
            mime_type=None,
            file_size=None,
            **kwargs
    ):
        super().__init__()
        self.file_id = file_id
        self.duration = duration
        self.performer = performer
        self.title = title
        self.mime_type = mime_type
        self.file_size = file_size
