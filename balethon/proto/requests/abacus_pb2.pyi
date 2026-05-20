from ..structs import peers_pb2 as _peers_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetMessageViews(_message.Message):
    __slots__ = ("peer", "mids", "increment")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MIDS_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    mids: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageId]
    increment: bool
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., mids: _Optional[_Iterable[_Union[_messaging_pb2.MessageId, _Mapping]]] = ..., increment: bool = ...) -> None: ...

class MessageSetReaction(_message.Message):
    __slots__ = ("peer", "rid", "code", "date")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    rid: int
    code: str
    date: int
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., code: _Optional[str] = ..., date: _Optional[int] = ...) -> None: ...
