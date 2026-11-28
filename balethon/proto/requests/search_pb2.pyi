from ..structs import search_pb2 as _search_pb2
from .. import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchPeer(_message.Message):
    __slots__ = ("query", "optimizations")
    QUERY_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    query: _containers.RepeatedCompositeFieldContainer[_search_pb2.SearchCondition]
    optimizations: _containers.RepeatedScalarFieldContainer[_enums_pb2.UpdateOptimization]
    def __init__(self, query: _Optional[_Iterable[_Union[_search_pb2.SearchCondition, _Mapping]]] = ..., optimizations: _Optional[_Iterable[_Union[_enums_pb2.UpdateOptimization, str]]] = ...) -> None: ...
