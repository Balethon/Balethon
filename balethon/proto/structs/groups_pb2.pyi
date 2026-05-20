from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from ..structs import peers_pb2 as _peers_pb2
from .. import enums_pb2 as _enums_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Group(_message.Message):
    __slots__ = ("id", "title", "members_count", "available_reactions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    members_count: int
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., members_count: _Optional[int] = ..., available_reactions: _Optional[_Iterable[str]] = ...) -> None: ...

class FullGroup(_message.Message):
    __slots__ = ("id", "title", "avatar", "owner_uid", "create_date", "group_type", "is_member", "members_count", "nick", "permissions", "default_permissions", "theme", "about", "members", "ex_info", "pin", "restriction", "available_reactions", "is_suspend", "linked_group_peer_id", "discussion_group_enabled")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    OWNER_UID_FIELD_NUMBER: _ClassVar[int]
    CREATE_DATE_FIELD_NUMBER: _ClassVar[int]
    GROUP_TYPE_FIELD_NUMBER: _ClassVar[int]
    IS_MEMBER_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    NICK_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    DEFAULT_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    THEME_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EX_INFO_FIELD_NUMBER: _ClassVar[int]
    PIN_FIELD_NUMBER: _ClassVar[int]
    RESTRICTION_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    IS_SUSPEND_FIELD_NUMBER: _ClassVar[int]
    LINKED_GROUP_PEER_ID_FIELD_NUMBER: _ClassVar[int]
    DISCUSSION_GROUP_ENABLED_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    avatar: _files_pb2.Avatar
    owner_uid: int
    create_date: int
    group_type: _enums_pb2.GroupType
    is_member: _collections_pb2.BoolValue
    members_count: _collections_pb2.Int32Value
    nick: _collections_pb2.StringValue
    permissions: Permissions
    default_permissions: Permissions
    theme: _collections_pb2.StringValue
    about: _collections_pb2.StringValue
    members: _containers.RepeatedCompositeFieldContainer[Member]
    ex_info: _peers_pb2.ExInfo
    pin: _messaging_pb2.MessageContainer
    restriction: _enums_pb2.Restriction
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    is_suspend: _collections_pb2.BoolValue
    linked_group_peer_id: _collections_pb2.Int32Value
    discussion_group_enabled: _collections_pb2.BoolValue
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., avatar: _Optional[_Union[_files_pb2.Avatar, _Mapping]] = ..., owner_uid: _Optional[int] = ..., create_date: _Optional[int] = ..., group_type: _Optional[_Union[_enums_pb2.GroupType, str]] = ..., is_member: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., members_count: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., nick: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., permissions: _Optional[_Union[Permissions, _Mapping]] = ..., default_permissions: _Optional[_Union[Permissions, _Mapping]] = ..., theme: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., about: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ..., members: _Optional[_Iterable[_Union[Member, _Mapping]]] = ..., ex_info: _Optional[_Union[_peers_pb2.ExInfo, _Mapping]] = ..., pin: _Optional[_Union[_messaging_pb2.MessageContainer, _Mapping]] = ..., restriction: _Optional[_Union[_enums_pb2.Restriction, str]] = ..., available_reactions: _Optional[_Iterable[str]] = ..., is_suspend: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., linked_group_peer_id: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ..., discussion_group_enabled: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class Permissions(_message.Message):
    __slots__ = ("see_message", "delete_message", "kick_user", "pin_message", "invite_user", "add_admin", "change_info", "send_message", "see_members", "edit_message", "send_media", "send_gif_stickers", "reply_to_story", "forward_message_from", "send_gift_packet", "start_call", "send_link_message", "send_forwarded_message", "add_story", "manage_call")
    SEE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DELETE_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    KICK_USER_FIELD_NUMBER: _ClassVar[int]
    PIN_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    INVITE_USER_FIELD_NUMBER: _ClassVar[int]
    ADD_ADMIN_FIELD_NUMBER: _ClassVar[int]
    CHANGE_INFO_FIELD_NUMBER: _ClassVar[int]
    SEND_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEE_MEMBERS_FIELD_NUMBER: _ClassVar[int]
    EDIT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_MEDIA_FIELD_NUMBER: _ClassVar[int]
    SEND_GIF_STICKERS_FIELD_NUMBER: _ClassVar[int]
    REPLY_TO_STORY_FIELD_NUMBER: _ClassVar[int]
    FORWARD_MESSAGE_FROM_FIELD_NUMBER: _ClassVar[int]
    SEND_GIFT_PACKET_FIELD_NUMBER: _ClassVar[int]
    START_CALL_FIELD_NUMBER: _ClassVar[int]
    SEND_LINK_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SEND_FORWARDED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ADD_STORY_FIELD_NUMBER: _ClassVar[int]
    MANAGE_CALL_FIELD_NUMBER: _ClassVar[int]
    see_message: bool
    delete_message: bool
    kick_user: bool
    pin_message: bool
    invite_user: bool
    add_admin: bool
    change_info: bool
    send_message: bool
    see_members: bool
    edit_message: bool
    send_media: bool
    send_gif_stickers: bool
    reply_to_story: bool
    forward_message_from: bool
    send_gift_packet: bool
    start_call: bool
    send_link_message: bool
    send_forwarded_message: bool
    add_story: bool
    manage_call: bool
    def __init__(self, see_message: bool = ..., delete_message: bool = ..., kick_user: bool = ..., pin_message: bool = ..., invite_user: bool = ..., add_admin: bool = ..., change_info: bool = ..., send_message: bool = ..., see_members: bool = ..., edit_message: bool = ..., send_media: bool = ..., send_gif_stickers: bool = ..., reply_to_story: bool = ..., forward_message_from: bool = ..., send_gift_packet: bool = ..., start_call: bool = ..., send_link_message: bool = ..., send_forwarded_message: bool = ..., add_story: bool = ..., manage_call: bool = ...) -> None: ...

class LoadMembersCondition(_message.Message):
    __slots__ = ("excepted_permissions", "contacts", "query")
    EXCEPTED_PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    QUERY_FIELD_NUMBER: _ClassVar[int]
    excepted_permissions: bool
    contacts: bool
    query: str
    def __init__(self, excepted_permissions: bool = ..., contacts: bool = ..., query: _Optional[str] = ...) -> None: ...

class Member(_message.Message):
    __slots__ = ("uid", "inviter_uid", "date", "is_admin", "promoter_user_id", "promoted_at", "permissions", "title")
    UID_FIELD_NUMBER: _ClassVar[int]
    INVITER_UID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    IS_ADMIN_FIELD_NUMBER: _ClassVar[int]
    PROMOTER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    PROMOTED_AT_FIELD_NUMBER: _ClassVar[int]
    PERMISSIONS_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    uid: int
    inviter_uid: int
    date: int
    is_admin: _collections_pb2.BoolValue
    promoter_user_id: int
    promoted_at: int
    permissions: Permissions
    title: str
    def __init__(self, uid: _Optional[int] = ..., inviter_uid: _Optional[int] = ..., date: _Optional[int] = ..., is_admin: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ..., promoter_user_id: _Optional[int] = ..., promoted_at: _Optional[int] = ..., permissions: _Optional[_Union[Permissions, _Mapping]] = ..., title: _Optional[str] = ...) -> None: ...
