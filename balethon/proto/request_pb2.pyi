import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("ws_request",)
    WS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    ws_request: WsRequest
    def __init__(self, ws_request: _Optional[_Union[WsRequest, _Mapping]] = ...) -> None: ...

class WsRequest(_message.Message):
    __slots__ = ("service_name", "method", "payload", "metadata", "index")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    method: str
    payload: bytes
    metadata: Metadata
    index: int
    def __init__(self, service_name: _Optional[str] = ..., method: _Optional[str] = ..., payload: _Optional[bytes] = ..., metadata: _Optional[_Union[Metadata, _Mapping]] = ..., index: _Optional[int] = ...) -> None: ...

class MetadataComplexValues(_message.Message):
    __slots__ = ("fixed64_value",)
    FIXED64_VALUE_FIELD_NUMBER: _ClassVar[int]
    fixed64_value: int
    def __init__(self, fixed64_value: _Optional[int] = ...) -> None: ...

class MetadataValues(_message.Message):
    __slots__ = ("string_value", "msg_value")
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    MSG_VALUE_FIELD_NUMBER: _ClassVar[int]
    string_value: str
    msg_value: MetadataComplexValues
    def __init__(self, string_value: _Optional[str] = ..., msg_value: _Optional[_Union[MetadataComplexValues, _Mapping]] = ...) -> None: ...

class MetadataKeyValues(_message.Message):
    __slots__ = ("key", "value")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    key: str
    value: MetadataValues
    def __init__(self, key: _Optional[str] = ..., value: _Optional[_Union[MetadataValues, _Mapping]] = ...) -> None: ...

class Metadata(_message.Message):
    __slots__ = ("key_values",)
    KEY_VALUES_FIELD_NUMBER: _ClassVar[int]
    key_values: _containers.RepeatedCompositeFieldContainer[MetadataKeyValues]
    def __init__(self, key_values: _Optional[_Iterable[_Union[MetadataKeyValues, _Mapping]]] = ...) -> None: ...

class KeepAliveRequest(_message.Message):
    __slots__ = ("payloads",)
    PAYLOADS_FIELD_NUMBER: _ClassVar[int]
    payloads: KeepAlive
    def __init__(self, payloads: _Optional[_Union[KeepAlive, _Mapping]] = ...) -> None: ...

class KeepAlive(_message.Message):
    __slots__ = ("value_should_2",)
    VALUE_SHOULD_2_FIELD_NUMBER: _ClassVar[int]
    value_should_2: int
    def __init__(self, value_should_2: _Optional[int] = ...) -> None: ...

class SetOnline(_message.Message):
    __slots__ = ("is_online", "duration")
    IS_ONLINE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    is_online: int
    duration: int
    def __init__(self, is_online: _Optional[int] = ..., duration: _Optional[int] = ...) -> None: ...

class EditName(_message.Message):
    __slots__ = ("name",)
    NAME_FIELD_NUMBER: _ClassVar[int]
    name: str
    def __init__(self, name: _Optional[str] = ...) -> None: ...

class SendMessage(_message.Message):
    __slots__ = ("peer", "rid", "message", "ex_peer")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    rid: int
    message: _struct_pb2.Message
    ex_peer: _struct_pb2.Peer
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., message: _Optional[_Union[_struct_pb2.Message, _Mapping]] = ..., ex_peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ...) -> None: ...

class UpdateMessage(_message.Message):
    __slots__ = ("peer", "rid", "updated_message")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    rid: int
    updated_message: _struct_pb2.Message
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., updated_message: _Optional[_Union[_struct_pb2.Message, _Mapping]] = ...) -> None: ...

class DeleteMessage(_message.Message):
    __slots__ = ("peer", "rids", "dates", "just_mine")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RIDS_FIELD_NUMBER: _ClassVar[int]
    DATES_FIELD_NUMBER: _ClassVar[int]
    JUST_MINE_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    rids: _containers.RepeatedScalarFieldContainer[int]
    dates: _struct_pb2.DeleteDates
    just_mine: bool
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., rids: _Optional[_Iterable[int]] = ..., dates: _Optional[_Union[_struct_pb2.DeleteDates, _Mapping]] = ..., just_mine: bool = ...) -> None: ...

class ForwardMessages(_message.Message):
    __slots__ = ("peer", "rid", "forwarded_messages")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    FORWARDED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    rid: _containers.RepeatedScalarFieldContainer[int]
    forwarded_messages: _containers.RepeatedCompositeFieldContainer[_struct_pb2.HistoryMessageIdentifier]
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., rid: _Optional[_Iterable[int]] = ..., forwarded_messages: _Optional[_Iterable[_Union[_struct_pb2.HistoryMessageIdentifier, _Mapping]]] = ...) -> None: ...

class GetMessageViews(_message.Message):
    __slots__ = ("peer", "mids", "increment")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MIDS_FIELD_NUMBER: _ClassVar[int]
    INCREMENT_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    mids: _containers.RepeatedCompositeFieldContainer[_struct_pb2.MessageId]
    increment: bool
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., mids: _Optional[_Iterable[_Union[_struct_pb2.MessageId, _Mapping]]] = ..., increment: bool = ...) -> None: ...

class MessageSetReaction(_message.Message):
    __slots__ = ("peer", "rid", "code", "date")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    rid: int
    code: str
    date: int
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., code: _Optional[str] = ..., date: _Optional[int] = ...) -> None: ...

class LoadHistory(_message.Message):
    __slots__ = ("peer", "date", "load_mode", "limit", "optimizations")
    PEER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LOAD_MODE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    date: int
    load_mode: int
    limit: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., date: _Optional[int] = ..., load_mode: _Optional[int] = ..., limit: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

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
    peer: _struct_pb2.Peer
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class LeaveGroup(_message.Message):
    __slots__ = ("group_peer", "rid", "optimizations", "make_orphan")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    MAKE_ORPHAN_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    make_orphan: bool
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ..., make_orphan: bool = ...) -> None: ...

class LoadUsers(_message.Message):
    __slots__ = ("user_peers",)
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    user_peers: _containers.RepeatedCompositeFieldContainer[_struct_pb2.UserOutPeer]
    def __init__(self, user_peers: _Optional[_Iterable[_Union[_struct_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class LoadFullUsers(_message.Message):
    __slots__ = ("user_peers",)
    USER_PEERS_FIELD_NUMBER: _ClassVar[int]
    user_peers: _containers.RepeatedCompositeFieldContainer[_struct_pb2.UserOutPeer]
    def __init__(self, user_peers: _Optional[_Iterable[_Union[_struct_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...

class GetFullGroup(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.GroupOutPeer
    def __init__(self, peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class SearchContacts(_message.Message):
    __slots__ = ("request", "optimizations")
    REQUEST_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    request: str
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, request: _Optional[str] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class PinMessage(_message.Message):
    __slots__ = ("sender_user_id", "group_peer", "date", "msg_rid")
    SENDER_USER_ID_FIELD_NUMBER: _ClassVar[int]
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MSG_RID_FIELD_NUMBER: _ClassVar[int]
    sender_user_id: int
    group_peer: _struct_pb2.GroupOutPeer
    date: int
    msg_rid: int
    def __init__(self, sender_user_id: _Optional[int] = ..., group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., date: _Optional[int] = ..., msg_rid: _Optional[int] = ...) -> None: ...

class PinMessages(_message.Message):
    __slots__ = ("peer", "message_id", "just_mine")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    JUST_MINE_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.Peer
    message_id: _struct_pb2.MessageId
    just_mine: bool
    def __init__(self, peer: _Optional[_Union[_struct_pb2.Peer, _Mapping]] = ..., message_id: _Optional[_Union[_struct_pb2.MessageId, _Mapping]] = ..., just_mine: bool = ...) -> None: ...

class UnPinMessages(_message.Message):
    __slots__ = ("peer", "message_ids", "all")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    peer: _struct_pb2.ExPeer
    message_ids: _containers.RepeatedCompositeFieldContainer[_struct_pb2.MessageId]
    all: bool
    def __init__(self, peer: _Optional[_Union[_struct_pb2.ExPeer, _Mapping]] = ..., message_ids: _Optional[_Iterable[_Union[_struct_pb2.MessageId, _Mapping]]] = ..., all: bool = ...) -> None: ...

class EditGroupAvatar(_message.Message):
    __slots__ = ("group_peer", "file_location", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    FILE_LOCATION_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    file_location: _struct_pb2.FileLocation
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., file_location: _Optional[_Union[_struct_pb2.FileLocation, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class RemoveGroupAvatar(_message.Message):
    __slots__ = ("group_peer", "rid", "optimizations", "avater_id")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    AVATER_ID_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    avater_id: int
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ..., avater_id: _Optional[int] = ...) -> None: ...

class EditGroupTitle(_message.Message):
    __slots__ = ("group_peer", "title", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    title: str
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., title: _Optional[str] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class EditGroupAbout(_message.Message):
    __slots__ = ("group_peer", "rid", "about", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    ABOUT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    rid: int
    about: str
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., about: _Optional[str] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class UnBanUser(_message.Message):
    __slots__ = ("group_peer", "user", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    user: _struct_pb2.UserOutPeer
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., user: _Optional[_Union[_struct_pb2.UserOutPeer, _Mapping]] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class KickUser(_message.Message):
    __slots__ = ("group_peer", "user", "rid", "optimizations")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    USER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    user: _struct_pb2.UserOutPeer
    rid: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., user: _Optional[_Union[_struct_pb2.UserOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class GetGroupInviteUrl(_message.Message):
    __slots__ = ("group_peer",)
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ...) -> None: ...

class InviteUsers(_message.Message):
    __slots__ = ("group_peer", "rid", "users")
    GROUP_PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    group_peer: _struct_pb2.GroupOutPeer
    rid: int
    users: _containers.RepeatedCompositeFieldContainer[_struct_pb2.UserOutPeer]
    def __init__(self, group_peer: _Optional[_Union[_struct_pb2.GroupOutPeer, _Mapping]] = ..., rid: _Optional[int] = ..., users: _Optional[_Iterable[_Union[_struct_pb2.UserOutPeer, _Mapping]]] = ...) -> None: ...
