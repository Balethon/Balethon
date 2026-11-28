from ..structs import peers_pb2 as _peers_pb2
from ..structs import messaging_pb2 as _messaging_pb2
from ..structs import collections_pb2 as _collections_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendInlineCallback(_message.Message):
    __slots__ = ("peer", "message_id", "data")
    PEER_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    peer: _peers_pb2.ExPeer
    message_id: _messaging_pb2.MessageId
    data: _collections_pb2.StringValue
    def __init__(self, peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., message_id: _Optional[_Union[_messaging_pb2.MessageId, _Mapping]] = ..., data: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...
