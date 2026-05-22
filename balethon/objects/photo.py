from . import Object


class Photo(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    @classmethod
    def from_protobuf(cls, protobuf_data):
        return cls(
            id=protobuf_data.file_id,
            width=protobuf_data.ext.document_ex_photo.w,
            height=protobuf_data.ext.document_ex_photo.h,
            size=protobuf_data.file_size
        )

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
