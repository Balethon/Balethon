from ..updates import messaging_pb2 as _messaging_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ComposedUpdates(_message.Message):
    __slots__ = ("message_sent", "message")
    MESSAGE_SENT_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    message_sent: bytes
    message: _messaging_pb2.Message
    def __init__(self, message_sent: _Optional[bytes] = ..., message: _Optional[_Union[_messaging_pb2.Message, _Mapping]] = ...) -> None: ...
