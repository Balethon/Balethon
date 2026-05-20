from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MetadataComplexValues(_message.Message):
    __slots__ = ("fixed64_value",)
    FIXED64_VALUE_FIELD_NUMBER: _ClassVar[int]
    fixed64_value: int
    def __init__(self, fixed64_value: _Optional[int] = ...) -> None: ...

class MetadataValues(_message.Message):
    __slots__ = ("string_value", "msg_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    MSG_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    msg_value: MetadataComplexValues
    def __init__(self, string_value: _Optional[str] = ..., msg_value: _Optional[_Union[MetadataComplexValues, _Mapping]] = ...) -> None: ...

class MetadataKeyValues(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: MetadataValues
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetadataValues, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("key_values",)
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    key_values: _containers.RepeatedCompositeFieldContainer[MetadataKeyValues]
    def __init__(self, key_values: _Optional[_Iterable[_Union[MetadataKeyValues, _Mapping]]] = ...) -> None: ...
