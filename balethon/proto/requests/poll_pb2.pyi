from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Vote(_message.Message):
    __slots__ = ("poll_id", "is_retract", "vote_at", "option_ids")
    POLL_ID_FIELD_NUMBER: _ClassVar[int]
    IS_RETRACT_FIELD_NUMBER: _ClassVar[int]
    VOTE_AT_FIELD_NUMBER: _ClassVar[int]
    OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    poll_id: int
    is_retract: bool
    vote_at: int
    option_ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, poll_id: _Optional[int] = ..., is_retract: bool = ..., vote_at: _Optional[int] = ..., option_ids: _Optional[_Iterable[int]] = ...) -> None: ...
