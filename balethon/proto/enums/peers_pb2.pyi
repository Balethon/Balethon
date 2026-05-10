from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class ExPeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EX_PEER_TYPE_UNKNOWN: _ClassVar[ExPeerType]
    EX_PEER_TYPE_PRIVATE: _ClassVar[ExPeerType]
    EX_PEER_TYPE_GROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_CHANNEL: _ClassVar[ExPeerType]
    EX_PEER_TYPE_BOT: _ClassVar[ExPeerType]
    EX_PEER_TYPE_SUPERGROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_THREAD: _ClassVar[ExPeerType]
EX_PEER_TYPE_UNKNOWN: ExPeerType
EX_PEER_TYPE_PRIVATE: ExPeerType
EX_PEER_TYPE_GROUP: ExPeerType
EX_PEER_TYPE_CHANNEL: ExPeerType
EX_PEER_TYPE_BOT: ExPeerType
EX_PEER_TYPE_SUPERGROUP: ExPeerType
EX_PEER_TYPE_THREAD: ExPeerType
