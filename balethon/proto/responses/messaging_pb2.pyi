from ..structs import messaging_pb2 as _messaging_pb2
from ..structs import groups_pb2 as _groups_pb2
from ..structs import users_pb2 as _users_pb2
from ..structs import peers_pb2 as _peers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LoadHistory(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageContainer]
    def __init__(self, history: _Optional[_Iterable[_Union[_messaging_pb2.MessageContainer, _Mapping]]] = ...) -> None: ...

class LoadDialogs(_message.Message):
    __slots__ = ("groups", "users", "dialogs", "user_peers", "group_peers")
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    DIALOGS_FIELD_NUMBER: _ClassVar[int]
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEERS_FIELD_NUMBER: _ClassVar[int]
    groups: _containers.RepeatedCompositeFieldContainer[_groups_pb2.Group]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.User]
    dialogs: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.Dialog]
    user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    group_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.GroupOutPeer]
    def __init__(self, groups: _Optional[_Iterable[_Union[_groups_pb2.Group, _Mapping]]] = ..., users: _Optional[_Iterable[_Union[_users_pb2.User, _Mapping]]] = ..., dialogs: _Optional[_Iterable[_Union[_messaging_pb2.Dialog, _Mapping]]] = ..., user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ..., group_peers: _Optional[_Iterable[_Union[_peers_pb2.GroupOutPeer, _Mapping]]] = ...) -> None: ...

class LoadPinnedMessages(_message.Message):
    __slots__ = ("pinned_messages",)
    PINNED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    pinned_messages: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageContainer]
    def __init__(self, pinned_messages: _Optional[_Iterable[_Union[_messaging_pb2.MessageContainer, _Mapping]]] = ...) -> None: ...
