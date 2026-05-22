from . import Object


class Voice(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    @classmethod
    def from_protobuf(cls, protobuf_data):
        return cls(
            id=protobuf_data.file_id,
            duration=protobuf_data.ext.document_ex_voice.duration,
            mime_type=protobuf_data.mime_type,
            size=protobuf_data.file_size
        )

    def __init__(
            self,
            id: str = None,
            duration: int = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.duration: int = duration
        self.mime_type: str = mime_type
        self.size: int = size
