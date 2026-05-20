from ..structs import files_pb2 as _files_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNasimFileUrl(_message.Message):
    __slots__ = ("file_url",)
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    file_url: _files_pb2.FileUrlDescription
    def __init__(self, file_url: _Optional[_Union[_files_pb2.FileUrlDescription, _Mapping]] = ...) -> None: ...

class GetNasimFileUploadUrl(_message.Message):
    __slots__ = ("file_id", "url", "duplicate", "chunk_size", "block_size")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    url: str
    duplicate: bool
    chunk_size: int
    block_size: int
    def __init__(self, file_id: _Optional[int] = ..., url: _Optional[str] = ..., duplicate: bool = ..., chunk_size: _Optional[int] = ..., block_size: _Optional[int] = ...) -> None: ...
