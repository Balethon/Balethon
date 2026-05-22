from balethon import objects
from . import Object


class Video(Object):
    attribute_names = [
        ("id", "file_id"),
        ("size", "file_size")
    ]

    @classmethod
    def from_protobuf(cls, protobuf_data):
        return cls(
            id=protobuf_data.file_id,
            width=protobuf_data.ext.document_ex_video.w,
            height=protobuf_data.ext.document_ex_video.h,
            duration=protobuf_data.ext.document_ex_video.duration,
            thumb=objects.Photo(
                width=protobuf_data.thumb.w,
                height=protobuf_data.thumb.h,
                file_size=len(protobuf_data.thumb.thumb)
            ),
            mime_type=protobuf_data.mime_type,
            size=protobuf_data.file_size
        )

    def __init__(
            self,
            id: str = None,
            width: int = None,
            height: int = None,
            duration: int = None,
            thumb: "objects.Photo" = None,
            mime_type: str = None,
            size: int = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: str = id
        self.width: int = width
        self.height: int = height
        self.duration: int = duration
        self.thumb: "objects.Photo" = thumb
        self.mime_type: str = mime_type
        self.size: int = size
