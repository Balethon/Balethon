from ..structs import users_pb2 as _users_pb2
from ..structs import peers_pb2 as _peers_pb2
from ..structs import groups_pb2 as _groups_pb2
from ..structs import search_pb2 as _search_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ResponseSearchPeer(_message.Message):
    __slots__ = ("search_results", "users", "groups", "user_peers", "group_peers")
    SEARCH_RESULTS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEERS_FIELD_NUMBER: _ClassVar[int]
    search_results: _containers.RepeatedCompositeFieldContainer[_search_pb2.PeerSearchResult]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.User]
    groups: _containers.RepeatedCompositeFieldContainer[_groups_pb2.Group]
    user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    group_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.GroupOutPeer]
    def __init__(self, search_results: _Optional[_Iterable[_Union[_search_pb2.PeerSearchResult, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_users_pb2.User, _Mapping]]] = ..., groups: _Optional[_Iterable[_Union[_groups_pb2.Group, _Mapping]]] = ..., user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ..., group_peers: _Optional[_Iterable[_Union[_peers_pb2.GroupOutPeer, _Mapping]]] = ...) -> None: ...
