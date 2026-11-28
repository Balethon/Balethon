from .. import enums_pb2 as _enums_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class InlineCallbackAnswer(_message.Message):
    __slots__ = ("text", "type")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    text: str
    type: _enums_pb2.InlineCallbackAnswerType
    def __init__(self, text: _Optional[str] = ..., type: _Optional[_Union[_enums_pb2.InlineCallbackAnswerType, str]] = ...) -> None: ...
