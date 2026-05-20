from ..structs import groups_pb2 as _groups_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import peers_pb2 as _peers_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetGroupPreview(_message.Message):
    __slots__ = ("group", "action")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    group: _groups_pb2.FullGroup
    action: int
    def __init__(self, group: _Optional[_Union[_groups_pb2.FullGroup, _Mapping]] = ..., action: _Optional[int] = ...) -> None: ...

class LoadGroupAvatars(_message.Message):
    __slots__ = ("avatars",)
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    avatars: _files_pb2.Avatars
    def __init__(self, avatars: _Optional[_Union[_files_pb2.Avatars, _Mapping]] = ...) -> None: ...

class JoinGroup(_message.Message):
    __slots__ = ("group", "seq")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    group: _groups_pb2.Group
    seq: int
    def __init__(self, group: _Optional[_Union[_groups_pb2.Group, _Mapping]] = ..., seq: _Optional[int] = ...) -> None: ...

class JoinPublicGroup(_message.Message):
    __slots__ = ("group", "seq")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    group: _groups_pb2.Group
    seq: int
    def __init__(self, group: _Optional[_Union[_groups_pb2.Group, _Mapping]] = ..., seq: _Optional[int] = ...) -> None: ...

class GetFullGroup(_message.Message):
    __slots__ = ("full_group",)
    FULL_GROUP_FIELD_NUMBER: _ClassVar[int]
    full_group: _groups_pb2.FullGroup
    def __init__(self, full_group: _Optional[_Union[_groups_pb2.FullGroup, _Mapping]] = ...) -> None: ...

class GetGroupMembersCount(_message.Message):
    __slots__ = ("members_count",)
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    members_count: int
    def __init__(self, members_count: _Optional[int] = ...) -> None: ...

class InviteUsers(_message.Message):
    __slots__ = ("not_added_user_peers",)
    NOT_ADDED_USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    not_added_user_peers: _containers.RepeatedCompositeFieldContainer[_peers_pb2.UserOutPeer]
    def __init__(self, not_added_user_peers: _Optional[_Iterable[_Union[_peers_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class LoadMembers(_message.Message):
    __slots__ = ("members", "next")
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    NEXT_FIELD_NUMBER: _ClassVar[int]
    members: _containers.RepeatedCompositeFieldContainer[_groups_pb2.Member]
    next: bytes
    def __init__(self, members: _Optional[_Iterable[_Union[_groups_pb2.Member, _Mapping]]] = ..., next: _Optional[bytes] = ...) -> None: ...

class GetGroupInviteUrl(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class RevokeInviteUrl(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class EditGroupAvatar(_message.Message):
    __slots__ = ("avatar", "seq", "state", "date")
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    avatar: _files_pb2.Avatar
    seq: int
    state: bytes
    date: int
    def __init__(self, avatar: _Optional[_Union[_files_pb2.Avatar, _Mapping]] = ..., seq: _Optional[int] = ..., state: _Optional[bytes] = ..., date: _Optional[int] = ...) -> None: ...
