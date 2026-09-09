from ..structs import poll_pb2 as _poll_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Vote(_message.Message):
    __slots__ = ("poll_result",)
    POLL_RESULT_FIELD_NUMBER: _ClassVar[int]
    poll_result: _poll_pb2.PollResult
    def __init__(self, poll_result: _Optional[_Union[_poll_pb2.PollResult, _Mapping]] = ...) -> None: ...
