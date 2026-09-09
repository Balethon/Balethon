from ..structs import peers_pb2 as _peers_pb2
from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EditName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class EditAbout(_message.Message):
    __slots__ = ("about",)
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    about: _collections_pb2.StringValue
    def __init__(self, about: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

class LoadAvatars(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.UserOutPeer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.UserOutPeer, _Mapping]] = ...) -> None: ...

class EditAvatar(_message.Message):
    __slots__ = ("file_location",)
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    file_location: _files_pb2.FileLocation
    def __init__(self, file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ...) -> None: ...

class RemoveAvatar(_message.Message):
    __slots__ = ("avatar_id",)
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    avatar_id: _collections_pb2.Int64Value
    def __init__(self, avatar_id: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class LoadUsers(_message.Message):
    __slots__ = ("user_peers",)
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    def __init__(self, user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class LoadFullUsers(_message.Message):
    __slots__ = ("user_peers",)
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    def __init__(self, user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class SearchContacts(_message.Message):
    __slots__ = ("request", "optimizations")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    request: str
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, request: _Optional[str] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...
