from ..structs import ketf_pb2 as _ketf_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SendInlineCallback(_message.Message):
    __slots__ = ("answer",)
    ANSWER_FIELD_NUMBER: _ClassVar[int]
    answer: _ketf_pb2.InlineCallbackAnswer
    def __init__(self, answer: _Optional[_Union[_ketf_pb2.InlineCallbackAnswer, _Mapping]] = ...) -> None: ...
