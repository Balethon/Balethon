from ..structs import peers_pb2 as _peers_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import collections_pb2 as _collections_pb2
from ..structs import groups_pb2 as _groups_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class JoinGroup(_message.Message):
    __slots__ = ("token", "optimizations")
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    token: str
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, token: _Optional[str] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class JoinPublicGroup(_message.Message):
    __slots__ = ("peer", "optimizations")
    PEER_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class LeaveGroup(_message.Message):
    __slots__ = ("group_peer", "rid", "optimizations", "make_orphan")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MAKE_ORPHAN_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    make_orphan: bool
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ..., make_orphan: bool = ...) -> None: ...

class GetFullGroup(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.GroupOutPeer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class PinMessage(_message.Message):
    __slots__ = ("sender_user_id", "group_peer", "date", "msg_rid")
    SENDER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MSG_RID_FIELD_NUMBER: _ClassVar[int]
    sender_user_id: int
    group_peer: _peers_pb2.GroupOutPeer
    date: int
    msg_rid: int
    def __init__(self, sender_user_id: _Optional[int] = ..., group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., date: _Optional[int] = ..., msg_rid: _Optional[int] = ...) -> None: ...

class EditGroupAvatar(_message.Message):
    __slots__ = ("group_peer", "file_location", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    file_location: _files_pb2.FileLocation
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., file_location: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class LoadGroupAvatars(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.GroupOutPeer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class RemoveGroupAvatar(_message.Message):
    __slots__ = ("group_peer", "rid", "optimizations", "avatar_id")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    AVATAR_ID_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    avatar_id: _collections_pb2.Int64Value
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ..., avatar_id: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ...) -> None: ...

class EditGroupTitle(_message.Message):
    __slots__ = ("group_peer", "title", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    title: str
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., title: _Optional[str] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class EditGroupAbout(_message.Message):
    __slots__ = ("group_peer", "rid", "about", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    rid: int
    about: str
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., about: _Optional[str] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class RevokeInviteUrl(_message.Message):
    __slots__ = ("group_peer",)
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class UnBanUser(_message.Message):
    __slots__ = ("group_peer", "user", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    user: _peers_pb2.UserOutPeer
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., user: _Optional[_Union[_peers_pb2.UserOutPeer, _Mapping]] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class KickUser(_message.Message):
    __slots__ = ("group_peer", "user", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    user: _peers_pb2.UserOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., user: _Optional[_Union[_peers_pb2.UserOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class GetGroupInviteUrl(_message.Message):
    __slots__ = ("group_peer",)
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class InviteUsers(_message.Message):
    __slots__ = ("group_peer", "rid", "users")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    rid: int
    users: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., users: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class SetMemberPermissions(_message.Message):
    __slots__ = ("group", "user", "permissions")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    group: _peers_pb2.GroupOutPeer
    user: _peers_pb2.UserOutPeer
    permissions: _groups_pb2.Permissions
    def __init__(self, group: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., user: _Optional[_Union[_peers_pb2.UserOutPeer, _Mapping]] = ..., permissions: _Optional[_Union[_groups_pb2.Permissions, _Mapping]] = ...) -> None: ...

class LoadMembers(_message.Message):
    __slots__ = ("group", "limit", "next", "condition")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    CONDITION_FIELD_NUMBER: _ClassVar[int]
    group: _peers_pb2.GroupOutPeer
    limit: int
    next: bytes
    condition: _groups_pb2.LoadMembersCondition
    def __init__(self, group: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., limit: _Optional[int] = ..., next: _Optional[bytes] = ..., condition: _Optional[_Union[_groups_pb2.LoadMembersCondition, _Mapping]] = ...) -> None: ...

class GetGroupMembersCount(_message.Message):
    __slots__ = ("group",)
    GROUP_FIELD_NUMBER: _ClassVar[int]
    group: _peers_pb2.GroupOutPeer
    def __init__(self, group: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class RemoveSinglePin(_message.Message):
    __slots__ = ("group_peer", "rid", "date")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    rid: int
    date: int
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., date: _Optional[int] = ...) -> None: ...

class RemovePin(_message.Message):
    __slots__ = ("group_peer",)
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class RemoveUserAdmin(_message.Message):
    __slots__ = ("group_peer", "user_peer")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    USER_PEER_FIELD_NUMBER: _ClassVar[int]
    group_peer: _peers_pb2.GroupOutPeer
    user_peer: _peers_pb2.UserOutPeer
    def __init__(self, group_peer: _Optional[_Union[_peers_pb2.GroupOutPeer, _Mapping]] = ..., user_peer: _Optional[_Union[_peers_pb2.UserOutPeer, _Mapping]] = ...) -> None: ...

class GetGroupPreview(_message.Message):
    __slots__ = ("token",)
    TOKEN_FIELD_NUMBER: _ClassVar[int]
    token: str
    def __init__(self, token: _Optional[str] = ...) -> None: ...
