from ..structs import collections_pb2 as _collections_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditParameter(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: _collections_pb2.StringValue
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...
