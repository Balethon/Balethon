from ..structs import peers_pb2 as _peers_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Message(_message.Message):
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
