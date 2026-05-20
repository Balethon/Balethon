from ..structs import messaging_pb2 as _messaging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMessageViews(_message.Message):
    __slots__ = ("containers",)
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    containers: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessagesViews]
    def __init__(self, containers: _Optional[_Iterable[_Union[_messaging_pb2.MessagesViews, _Mapping]]] = ...) -> None: ...
