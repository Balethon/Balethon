from ..structs import collections_pb2 as _collections_pb2
from ..structs import files_pb2 as _files_pb2
from ..structs import groups_pb2 as _groups_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from ..structs import peers_pb2 as _peers_pb2
from ..structs import users_pb2 as _users_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Response(_message.Message):
    __slots__ = ("ws_response", "ws_update")
    WS_RESPONSE_FIELD_NUMBER: _ClassVar[int]
    WS_UPDATE_FIELD_NUMBER: _ClassVar[int]
    ws_response: WsResponse
    ws_update: WsUpdate
    def __init__(self, ws_response: _Optional[_Union[WsResponse, _Mapping]] = ..., ws_update: _Optional[_Union[WsUpdate, _Mapping]] = ...) -> None: ...

class WsResponse(_message.Message):
    __slots__ = ("error", "response", "index")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    error: WsError
    response: bytes
    index: int
    def __init__(self, error: _Optional[_Union[WsError, _Mapping]] = ..., response: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class WsError(_message.Message):
    __slots__ = ("code", "message", "details")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    details: _collections_pb2.MapValue
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Union[_collections_pb2.MapValue, _Mapping]] = ...) -> None: ...

class WsUpdate(_message.Message):
    __slots__ = ("update",)
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update: Update
    def __init__(self, update: _Optional[_Union[Update, _Mapping]] = ...) -> None: ...

class Update(_message.Message):
    __slots__ = ("composed_update",)
    COMPOSED_UPDATE_FIELD_NUMBER: _ClassVar[int]
    composed_update: ComposedUpdate
    def __init__(self, composed_update: _Optional[_Union[ComposedUpdate, _Mapping]] = ...) -> None: ...

class ComposedUpdate(_message.Message):
    __slots__ = ("message_sent", "message")
    MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_sent: bytes
    message: UpdateMessage
    def __init__(self, message_sent: _Optional[bytes] = ..., message: _Optional[_Union[UpdateMessage, _Mapping]] = ...) -> None: ...

class UpdateMessage(_message.Message):
    __slots__ = ("peer", "sender_uid", "date", "rid", "message", "quoted_message", "previous_message_id")
    PEER_FIELD_NUMBER: _ClassVar[int]
    SENDER_UID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    QUOTED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    PREVIOUS_MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    sender_uid: int
    date: int
    rid: int
    message: _messaging_pb2.Message
    quoted_message: _messaging_pb2.QuotedMessage
    previous_message_id: _messaging_pb2.MessageId
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., sender_uid: _Optional[int] = ..., date: _Optional[int] = ..., rid: _Optional[int] = ..., message: _Optional[_Union[_messaging_pb2.Message, _Mapping]] = ..., quoted_message: _Optional[_Union[_messaging_pb2.QuotedMessage, _Mapping]] = ..., previous_message_id: _Optional[_Union[_messaging_pb2.MessageId, _Mapping]] = ...) -> None: ...

class GetMessageViews(_message.Message):
    __slots__ = ("containers",)
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    containers: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessagesViews]
    def __init__(self, containers: _Optional[_Iterable[_Union[_messaging_pb2.MessagesViews, _Mapping]]] = ...) -> None: ...

class LoadHistory(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageContainer]
    def __init__(self, history: _Optional[_Iterable[_Union[_messaging_pb2.MessageContainer, _Mapping]]] = ...) -> None: ...

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

class LoadUsers(_message.Message):
    __slots__ = ("users",)
    USERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedCompositeFieldContainer[_users_pb2.User]
    def __init__(self, users: _Optional[_Iterable[_Union[_users_pb2.User, _Mapping]]] = ...) -> None: ...

class GetFullGroup(_message.Message):
    __slots__ = ("full_group",)
    FULL_GROUP_FIELD_NUMBER: _ClassVar[int]
    full_group: _groups_pb2.FullGroup
    def __init__(self, full_group: _Optional[_Union[_groups_pb2.FullGroup, _Mapping]] = ...) -> None: ...

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

class GetGroupMembersCount(_message.Message):
    __slots__ = ("members_count",)
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    members_count: int
    def __init__(self, members_count: _Optional[int] = ...) -> None: ...

class GetNasimFileUploadUrl(_message.Message):
    __slots__ = ("file_id", "url", "duplicate", "chunk_size", "block_size")
    FILE_ID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    DUPLICATE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    BLOCK_SIZE_FIELD_NUMBER: _ClassVar[int]
    file_id: int
    url: str
    duplicate: bool
    chunk_size: int
    block_size: int
    def __init__(self, file_id: _Optional[int] = ..., url: _Optional[str] = ..., duplicate: bool = ..., chunk_size: _Optional[int] = ..., block_size: _Optional[int] = ...) -> None: ...

class StartPhoneAuth(_message.Message):
    __slots__ = ("transaction_hash", "is_registered", "sent_code_type", "code_expiration_date", "next_send_code_type", "next_send_code_wait_time", "code_timeout")
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    SENT_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEND_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEND_CODE_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    CODE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: str
    is_registered: bool
    sent_code_type: int
    code_expiration_date: _collections_pb2.Int64Value
    next_send_code_type: int
    next_send_code_wait_time: _collections_pb2.Int64Value
    code_timeout: _collections_pb2.Int32Value
    def __init__(self, transaction_hash: _Optional[str] = ..., is_registered: bool = ..., sent_code_type: _Optional[int] = ..., code_expiration_date: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., next_send_code_type: _Optional[int] = ..., next_send_code_wait_time: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., code_timeout: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class Auth(_message.Message):
    __slots__ = ("user", "jwt")
    USER_FIELD_NUMBER: _ClassVar[int]
    JWT_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.User
    jwt: _collections_pb2.StringValue
    def __init__(self, user: _Optional[_Union[_users_pb2.User, _Mapping]] = ..., jwt: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

class LoadGroupAvatars(_message.Message):
    __slots__ = ("avatars",)
    AVATARS_FIELD_NUMBER: _ClassVar[int]
    avatars: _files_pb2.Avatars
    def __init__(self, avatars: _Optional[_Union[_files_pb2.Avatars, _Mapping]] = ...) -> None: ...

class LoadPinnedMessages(_message.Message):
    __slots__ = ("pinned_messages",)
    PINNED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    pinned_messages: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageContainer]
    def __init__(self, pinned_messages: _Optional[_Iterable[_Union[_messaging_pb2.MessageContainer, _Mapping]]] = ...) -> None: ...

class GetNasimFileUrl(_message.Message):
    __slots__ = ("file_url",)
    FILE_URL_FIELD_NUMBER: _ClassVar[int]
    file_url: _files_pb2.FileUrlDescription
    def __init__(self, file_url: _Optional[_Union[_files_pb2.FileUrlDescription, _Mapping]] = ...) -> None: ...

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

class GetGroupPreview(_message.Message):
    __slots__ = ("group", "action")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    group: _groups_pb2.FullGroup
    action: int
    def __init__(self, group: _Optional[_Union[_groups_pb2.FullGroup, _Mapping]] = ..., action: _Optional[int] = ...) -> None: ...
