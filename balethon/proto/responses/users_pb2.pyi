from ..structs import users_pb2 as _users_pb2
from ..structs import peers_pb2 as _peers_pb2
from ..structs import groups_pb2 as _groups_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadUsers(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.User]
    def __init__(self, users: _Optional[_Iterable[_Union[_users_pb2.User, _Mapping]]] = ...) -> None: ...

class SearchContacts(_message.Message):
    __slots__ = ("users", "user_peers", "groups", "group_peers")
    USERS_FIELD_NUMBER: _ClassVar[int]
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.User]
    user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    groups: _containers.RepeatedCompositeFieldContainer[_groups_pb2.Group]
    group_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.GroupOutPeer]
    def __init__(self, users: _Optional[_Iterable[_Union[_users_pb2.User, _Mapping]]] = ..., user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[_groups_pb2.Group, _Mapping]]] = ..., group_peers: _Optional[_Iterable[_Union[_peers_pb2.GroupOutPeer, _Mapping]]] = ...) -> None: ...
