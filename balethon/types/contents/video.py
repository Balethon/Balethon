from ..object import Object


class Video(Object):

    def __init__(
            self,
            file_id=None,
            width=None,
            height=None,
            duration=None,
            thumb=None,
            mime_type=None,
            file_size=None,
            **kwargs
    ):
        super().__init__()
        self.file_id = file_id
        self.width = width
        self.height = height
        self.duration = duration
        self.thumb = thumb
        self.mime_type = mime_type
        self.file_size = file_size
