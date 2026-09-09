from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class OptionResult(_message.Message):
    __slots__ = ("option_id", "votes_count")
    OPTION_ID_FIELD_NUMBER: _ClassVar[int]
    VOTES_COUNT_FIELD_NUMBER: _ClassVar[int]
    option_id: int
    votes_count: int
    def __init__(self, option_id: _Optional[int] = ..., votes_count: _Optional[int] = ...) -> None: ...

class PollResult(_message.Message):
    __slots__ = ("option_results", "recent_voters", "chosen_option_ids", "is_closed", "poll_id", "voters_count")
    OPTION_RESULTS_FIELD_NUMBER: _ClassVar[int]
    RECENT_VOTERS_FIELD_NUMBER: _ClassVar[int]
    CHOSEN_OPTION_IDS_FIELD_NUMBER: _ClassVar[int]
    IS_CLOSED_FIELD_NUMBER: _ClassVar[int]
    POLL_ID_FIELD_NUMBER: _ClassVar[int]
    VOTERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    option_results: _containers.RepeatedCompositeFieldContainer[OptionResult]
    recent_voters: _containers.RepeatedScalarFieldContainer[int]
    chosen_option_ids: _containers.RepeatedScalarFieldContainer[int]
    is_closed: bool
    poll_id: int
    voters_count: int
    def __init__(self, option_results: _Optional[_Iterable[_Union[OptionResult, _Mapping]]] = ..., recent_voters: _Optional[_Iterable[int]] = ..., chosen_option_ids: _Optional[_Iterable[int]] = ..., is_closed: bool = ..., poll_id: _Optional[int] = ..., voters_count: _Optional[int] = ...) -> None: ...
