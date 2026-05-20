from ..structs import collections_pb2 as _collections_pb2
from .. import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FastThumb(_message.Message):
    __slots__ = ("w", "h", "thumb")
    W_FIELD_NUMBER: _ClassVar[int]
    H_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    w: int
    h: int
    thumb: bytes
    def __init__(self, w: _Optional[int] = ..., h: _Optional[int] = ..., thumb: _Optional[bytes] = ...) -> None: ...

class ImageLocation(_message.Message):
    __slots__ = ("file_location", "width", "height", "file_size")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_location: FileLocation
    width: int
    height: int
    file_size: int
    def __init__(self, file_location: _Optional[_Union[FileLocation, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., file_size: _Optional[int] = ...) -> None: ...

class FileLocation(_message.Message):
    __slots__ = ("file_id", "access_hash", "file_storage_version")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    FILE_STORAGE_VERSION_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    access_hash: int
    file_storage_version: _collections_pb2.Int32Value
    def __init__(self, file_id: _Optional[int] = ..., access_hash: _Optional[int] = ..., file_storage_version: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class AvatarImage(_message.Message):
    __slots__ = ("file_location", "width", "height", "file_size")
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    FILE_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_location: FileLocation
    width: int
    height: int
    file_size: int
    def __init__(self, file_location: _Optional[_Union[FileLocation, _Mapping]] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., file_size: _Optional[int] = ...) -> None: ...

class Avatar(_message.Message):
    __slots__ = ("small_image", "large_image", "full_image", "id", "date")
    SMALL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    LARGE_IMAGE_FIELD_NUMBER: _ClassVar[int]
    FULL_IMAGE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    small_image: AvatarImage
    large_image: AvatarImage
    full_image: AvatarImage
    id: _collections_pb2.Int64Value
    date: _collections_pb2.Int64Value
    def __init__(self, small_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., large_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., full_image: _Optional[_Union[AvatarImage, _Mapping]] = ..., id: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., date: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class SendTypeValue(_message.Message):
    __slots__ = ("type",)
    TYPE_FIELD_NUMBER: _ClassVar[int]
    type: _enums_pb2.SendType
    def __init__(self, type: _Optional[_Union[_enums_pb2.SendType, str]] = ...) -> None: ...

class Avatars(_message.Message):
    __slots__ = ("avatars",)
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    avatars: _containers.RepeatedCompositeFieldContainer[Avatar]
    def __init__(self, avatars: _Optional[_Iterable[_Union[Avatar, _Mapping]]] = ...) -> None: ...

class FileUrlDescription(_message.Message):
    __slots__ = ("file_id", "url", "timeout", "unsigned_url", "chunk_size")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    UNSIGNED_URL_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    url: str
    timeout: int
    unsigned_url: str
    chunk_size: _collections_pb2.Int32Value
    def __init__(self, file_id: _Optional[int] = ..., url: _Optional[str] = ..., timeout: _Optional[int] = ..., unsigned_url: _Optional[str] = ..., chunk_size: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ...) -> None: ...
