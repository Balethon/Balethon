from ..structs import peers_pb2 as _peers_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendMessage(_message.Message):
    __slots__ = ("peer", "rid", "message", "ex_peer")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    rid: int
    message: _messaging_pb2.Message
    ex_peer: _peers_pb2.Peer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., message: _Optional[_Union[_messaging_pb2.Message, _Mapping]] = ..., ex_peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ...) -> None: ...

class UpdateMessage(_message.Message):
    __slots__ = ("peer", "rid", "updated_message")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    UPDATED_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    rid: int
    updated_message: _messaging_pb2.Message
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., rid: _Optional[int] = ..., updated_message: _Optional[_Union[_messaging_pb2.Message, _Mapping]] = ...) -> None: ...

class DeleteMessage(_message.Message):
    __slots__ = ("peer", "rids", "dates", "just_mine")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RIDS_FIELD_NUMBER: _ClassVar[int]
    DATES_FIELD_NUMBER: _ClassVar[int]
    JUST_MINE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    rids: _containers.RepeatedScalarFieldContainer[int]
    dates: _messaging_pb2.DeleteDates
    just_mine: bool
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., rids: _Optional[_Iterable[int]] = ..., dates: _Optional[_Union[_messaging_pb2.DeleteDates, _Mapping]] = ..., just_mine: bool = ...) -> None: ...

class ForwardMessages(_message.Message):
    __slots__ = ("peer", "rid", "forwarded_messages")
    PEER_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    FORWARDED_MESSAGES_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    rid: _containers.RepeatedScalarFieldContainer[int]
    forwarded_messages: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.HistoryMessageIdentifier]
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., rid: _Optional[_Iterable[int]] = ..., forwarded_messages: _Optional[_Iterable[_Union[_messaging_pb2.HistoryMessageIdentifier, _Mapping]]] = ...) -> None: ...

class LoadHistory(_message.Message):
    __slots__ = ("peer", "date", "load_mode", "limit", "optimizations")
    PEER_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    LOAD_MODE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    date: int
    load_mode: int
    limit: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., date: _Optional[int] = ..., load_mode: _Optional[int] = ..., limit: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ...) -> None: ...

class PinMessages(_message.Message):
    __slots__ = ("peer", "message_id", "just_mine")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    JUST_MINE_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.Peer
    message_id: _messaging_pb2.MessageId
    just_mine: bool
    def __init__(self, peer: _Optional[_Union[_peers_pb2.Peer, _Mapping]] = ..., message_id: _Optional[_Union[_messaging_pb2.MessageId, _Mapping]] = ..., just_mine: bool = ...) -> None: ...

class UnPinMessages(_message.Message):
    __slots__ = ("peer", "message_ids", "all")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_IDS_FIELD_NUMBER: _ClassVar[int]
    ALL_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.ExPeer
    message_ids: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.MessageId]
    all: bool
    def __init__(self, peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., message_ids: _Optional[_Iterable[_Union[_messaging_pb2.MessageId, _Mapping]]] = ..., all: bool = ...) -> None: ...

class LoadPinnedMessages(_message.Message):
    __slots__ = ("peer",)
    PEER_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.ExPeer
    def __init__(self, peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ...) -> None: ...

class SendMultiMediaMessage(_message.Message):
    __slots__ = ("peer", "multi_media", "grouped_id")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MULTI_MEDIA_FIELD_NUMBER: _ClassVar[int]
    GROUPED_ID_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.ExPeer
    multi_media: _containers.RepeatedCompositeFieldContainer[_messaging_pb2.SingleMedia]
    grouped_id: int
    def __init__(self, peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., multi_media: _Optional[_Iterable[_Union[_messaging_pb2.SingleMedia, _Mapping]]] = ..., grouped_id: _Optional[int] = ...) -> None: ...

class LoadDialogs(_message.Message):
    __slots__ = ("min_date", "limit", "optimizations", "dialog_type", "exclude_pinned_dialogs", "archive_filter")
    MIN_DATE_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OPTIMIZATIONS_FIELD_NUMBER: _ClassVar[int]
    DIALOG_TYPE_FIELD_NUMBER: _ClassVar[int]
    EXCLUDE_PINNED_DIALOGS_FIELD_NUMBER: _ClassVar[int]
    ARCHIVE_FILTER_FIELD_NUMBER: _ClassVar[int]
    min_date: int
    limit: int
    optimizations: _containers.RepeatedScalarFieldContainer[int]
    dialog_type: int
    exclude_pinned_dialogs: bool
    archive_filter: int
    def __init__(self, min_date: _Optional[int] = ..., limit: _Optional[int] = ..., optimizations: _Optional[_Iterable[int]] = ..., dialog_type: _Optional[int] = ..., exclude_pinned_dialogs: bool = ..., archive_filter: _Optional[int] = ...) -> None: ...
