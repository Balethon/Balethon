from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Int64Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...

class BoolValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: bool
    def __init__(self, value: bool = ...) -> None: ...

class StringValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: str
    def __init__(self, value: _Optional[str] = ...) -> None: ...

class BytesValue(_message.Message):
    __slots__ = ("Value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    Value: str
    def __init__(self, Value: _Optional[str] = ...) -> None: ...

class DoubleValue(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: float
    def __init__(self, value: _Optional[float] = ...) -> None: ...

class ArrayValue(_message.Message):
    __slots__ = ("array",)
    ARRAY_FIELD_NUMBER: _ClassVar[int]
    array: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, array: _Optional[_Iterable[bytes]] = ...) -> None: ...

class RawValue(_message.Message):
    __slots__ = ("string_value", "boolean_value", "int32_value", "int64_value", "double_value", "array_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    BOOLEAN_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT32_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    ARRAY_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: StringValue
    boolean_value: BoolValue
    int32_value: Int32Value
    int64_value: Int64Value
    double_value: DoubleValue
    array_value: ArrayValue
    def __init__(self, string_value: _Optional[_Union[StringValue, _Mapping]] = ..., boolean_value: _Optional[_Union[BoolValue, _Mapping]] = ..., int32_value: _Optional[_Union[Int32Value, _Mapping]] = ..., int64_value: _Optional[_Union[Int64Value, _Mapping]] = ..., double_value: _Optional[_Union[DoubleValue, _Mapping]] = ..., array_value: _Optional[_Union[ArrayValue, _Mapping]] = ...) -> None: ...

class MapValueItem(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: RawValue
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[RawValue, _Mapping]] = ...) -> None: ...

class MapValue(_message.Message):
    __slots__ = ("items",)
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    items: _containers.RepeatedCompositeFieldContainer[MapValueItem]
    def __init__(self, items: _Optional[_Iterable[_Union[MapValueItem, _Mapping]]] = ...) -> None: ...

class Int32Value(_message.Message):
    __slots__ = ("value",)
    VALUE_FIELD_NUMBER: _ClassVar[int]
    value: int
    def __init__(self, value: _Optional[int] = ...) -> None: ...
