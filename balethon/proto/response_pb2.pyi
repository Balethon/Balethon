import struct_pb2 as _struct_pb2
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
    error: bytes
    response: bytes
    index: int
    def __init__(self, error: _Optional[bytes] = ..., response: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

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
    peer: _struct_pb2.Peer
    sender_uid: int
    date: int
    rid: int
    message: _struct_pb2.Message
    quoted_message: _struct_pb2.QuotedMessage
    previous_message_id: _struct_pb2.MessageId
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., sender_uid: _Optional[int] = ..., date: _Optional[int] = ..., rid: _Optional[int] = ..., message: _Optional[_Union[_struct_pb2.Message, _Mapping]] = ..., quoted_message: _Optional[_Union[_struct_pb2.QuotedMessage, _Mapping]] = ..., previous_message_id: _Optional[_Union[_struct_pb2.MessageId, _Mapping]] = ...) -> None: ...

class GetMessageViews(_message.Message):
    __slots__ = ("containers",)
    CONTAINERS_FIELD_NUMBER: _ClassVar[int]
    containers: _containers.RepeatedCompositeFieldContainer[_struct_pb2.MessagesViews]
    def __init__(self, containers: _Optional[_Iterable[_Union[_struct_pb2.MessagesViews, _Mapping]]] = ...) -> None: ...

class LoadHistory(_message.Message):
    __slots__ = ("history",)
    HISTORY_FIELD_NUMBER: _ClassVar[int]
    history: _containers.RepeatedCompositeFieldContainer[_struct_pb2.MessageContainer]
    def __init__(self, history: _Optional[_Iterable[_Union[_struct_pb2.MessageContainer, _Mapping]]] = ...) -> None: ...

class JoinGroup(_message.Message):
    __slots__ = ("group", "seq")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    group: _struct_pb2.Group
    seq: int
    def __init__(self, group: _Optional[_Union[_struct_pb2.Group, _Mapping]] = ..., seq: _Optional[int] = ...) -> None: ...

class JoinPublicGroup(_message.Message):
    __slots__ = ("group", "seq")
    GROUP_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    group: _struct_pb2.Group
    seq: int
    def __init__(self, group: _Optional[_Union[_struct_pb2.Group, _Mapping]] = ..., seq: _Optional[int] = ...) -> None: ...

class GetFullGroup(_message.Message):
    __slots__ = ("full_group",)
    FULL_GROUP_FIELD_NUMBER: _ClassVar[int]
    full_group: _struct_pb2.FullGroup
    def __init__(self, full_group: _Optional[_Union[_struct_pb2.FullGroup, _Mapping]] = ...) -> None: ...

class SearchContacts(_message.Message):
    __slots__ = ("users", "user_peers", "groups", "group_peers")
    USERS_FIELD_NUMBER: _ClassVar[int]
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    GROUPS_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEERS_FIELD_NUMBER: _ClassVar[int]
    users: _containers.RepeatedScalarFieldContainer[int]
    user_peers: _containers.RepeatedScalarFieldContainer[int]
    groups: _containers.RepeatedScalarFieldContainer[int]
    group_peers: _containers.RepeatedCompositeFieldContainer[_struct_pb2.GroupOutPeer]
    def __init__(self, users: _Optional[_Iterable[int]] = ..., user_peers: _Optional[_Iterable[int]] = ..., groups: _Optional[_Iterable[int]] = ..., group_peers: _Optional[_Iterable[_Union[_struct_pb2.GroupOutPeer, _Mapping]]] = ...) -> None: ...

class EditGroupAvatar(_message.Message):
    __slots__ = ("avatar", "seq", "state", "date")
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    avatar: _struct_pb2.Avatar
    seq: int
    state: bytes
    date: int
    def __init__(self, avatar: _Optional[_Union[_struct_pb2.Avatar, _Mapping]] = ..., seq: _Optional[int] = ..., state: _Optional[bytes] = ..., date: _Optional[int] = ...) -> None: ...

class GetGroupInviteUrl(_message.Message):
    __slots__ = ("url",)
    URL_FIELD_NUMBER: _ClassVar[int]
    url: str
    def __init__(self, url: _Optional[str] = ...) -> None: ...

class InviteUsers(_message.Message):
    __slots__ = ("not_added_user_peers",)
    NOT_ADDED_USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    not_added_user_peers: _containers.RepeatedCompositeFieldContainer[_struct_pb2.UserOutPeer]
    def __init__(self, not_added_user_peers: _Optional[_Iterable[_Union[_struct_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...
