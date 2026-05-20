from ..structs import peers_pb2 as _peers_pb2
from .. import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetOnline(_message.Message):
    __slots__ = ("is_online", "duration")
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    is_online: int
    duration: int
    def __init__(self, is_online: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class Typing(_message.Message):
    __slots__ = ("peer", "typing_type")
    PEER_FIELD_NUMBER: _ClassVar[int]
    TYPING_TYPE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.OutPeer
    typing_type: _enums_pb2.TypingType
    def __init__(self, peer: _Optional[_Union[_peers_pb2.OutPeer, _Mapping]] = ..., typing_type: _Optional[_Union[_enums_pb2.TypingType, str]] = ...) -> None: ...
