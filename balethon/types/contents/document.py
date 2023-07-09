from ..object import Object


class Document(Object):

    def __init__(
            self,
            file_id=None,
            thumb=None,
            file_name=None,
            mime_type=None,
            file_size=None,
            **kwargs
    ):
        super().__init__()
        self.file_id = file_id
        self.thumb = thumb
        self.file_name = file_name
        self.mime_type = mime_type
        self.file_size = file_size
