from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Peer(_message.Message):
    __slots__ = ("type", "id")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    type: int
    id: int
    def __init__(self, type: _Optional[int] = ..., id: _Optional[int] = ...) -> None: ...

class TextMessage(_message.Message):
    __slots__ = ("text", "mentions")
    TEXT_FIELD_NUMBER: _ClassVar[int]
    MENTIONS_FIELD_NUMBER: _ClassVar[int]
    text: str
    mentions: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, text: _Optional[str] = ..., mentions: _Optional[_Iterable[int]] = ...) -> None: ...

class Message(_message.Message):
    __slots__ = ("text_message",)
    TEXT_MESSAGE_FIELD_NUMBER: _ClassVar[int]
    text_message: TextMessage
    def __init__(self, text_message: _Optional[_Union[TextMessage, _Mapping]] = ...) -> None: ...

class DeleteDates(_message.Message):
    __slots__ = ("dates",)
    DATES_FIELD_NUMBER: _ClassVar[int]
    dates: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, dates: _Optional[_Iterable[int]] = ...) -> None: ...

class MessageId(_message.Message):
    __slots__ = ("date", "rid", "seq")
    DATE_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    SEQ_FIELD_NUMBER: _ClassVar[int]
    date: int
    rid: int
    seq: int
    def __init__(self, date: _Optional[int] = ..., rid: _Optional[int] = ..., seq: _Optional[int] = ...) -> None: ...

class GroupOutPeer(_message.Message):
    __slots__ = ("group_id", "access_hash")
    GROUP_ID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    group_id: int
    access_hash: int
    def __init__(self, group_id: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class UserOutPeer(_message.Message):
    __slots__ = ("uid", "access_hash")
    UID_FIELD_NUMBER: _ClassVar[int]
    ACCESS_HASH_FIELD_NUMBER: _ClassVar[int]
    uid: int
    access_hash: int
    def __init__(self, uid: _Optional[int] = ..., access_hash: _Optional[int] = ...) -> None: ...

class MessageContainer(_message.Message):
    __slots__ = ("sender_uid", "rid", "date", "message")
    SENDER_UID_FIELD_NUMBER: _ClassVar[int]
    RID_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    sender_uid: int
    rid: int
    date: int
    message: Message
    def __init__(self, sender_uid: _Optional[int] = ..., rid: _Optional[int] = ..., date: _Optional[int] = ..., message: _Optional[_Union[Message, _Mapping]] = ...) -> None: ...

class Group(_message.Message):
    __slots__ = ("id", "title", "members_count", "available_reactions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    members_count: int
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., members_count: _Optional[int] = ..., available_reactions: _Optional[_Iterable[str]] = ...) -> None: ...

class FullGroup(_message.Message):
    __slots__ = ("id", "title", "members_count", "available_reactions")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_COUNT_FIELD_NUMBER: _ClassVar[int]
    AVAILABLE_REACTIONS_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    members_count: int
    available_reactions: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., members_count: _Optional[int] = ..., available_reactions: _Optional[_Iterable[str]] = ...) -> None: ...

class MessagesViews(_message.Message):
    __slots__ = ("mid", "views")
    MID_FIELD_NUMBER: _ClassVar[int]
    VIEWS_FIELD_NUMBER: _ClassVar[int]
    mid: MessageId
    views: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, mid: _Optional[_Union[MessageId, _Mapping]] = ..., views: _Optional[_Iterable[int]] = ...) -> None: ...
