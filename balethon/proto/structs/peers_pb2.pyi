from .. import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Peer(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class ExPeer(_message.Message):
    __slots__ = ("type", "id", "access_hash")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    access_hash: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class ExInfo(_message.Message):
    __slots__ = ("ex_peer_type",)
    EX_PEER_TYPE_FIELD_NUMBER: _ClassVar[int]
    ex_peer_type: _enums_pb2.ExPeerType
    def __init__(self, ex_peer_type: _Optional[_Union[_enums_pb2.ExPeerType, str]] = ...) -> None: ...

class OutPeer(_message.Message):
    __slots__ = ("type", "id", "access_hash")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    access_hash: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class GroupOutPeer(_message.Message):
    __slots__ = ("group_id", "access_hash")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    access_hash: int
    def __init__(self, group_id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class UserOutPeer(_message.Message):
    __slots__ = ("uid", "access_hash")
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    uid: int
    access_hash: int
    def __init__(self, uid: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...
