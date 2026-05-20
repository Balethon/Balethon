from ..structs import collections_pb2 as _collections_pb2
from ..structs import users_pb2 as _users_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartPhoneAuth(_message.Message):
    __slots__ = ("transaction_hash", "is_registered", "sent_code_type", "code_expiration_date", "next_send_code_type", "next_send_code_wait_time", "code_timeout")
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    IS_REGISTERED_FIELD_NUMBER: _ClassVar[int]
    SENT_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    CODE_EXPIRATION_DATE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEND_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NEXT_SEND_CODE_WAIT_TIME_FIELD_NUMBER: _ClassVar[int]
    CODE_TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: str
    is_registered: bool
    sent_code_type: int
    code_expiration_date: _collections_pb2.Int64Value
    next_send_code_type: int
    next_send_code_wait_time: _collections_pb2.Int64Value
    code_timeout: _collections_pb2.Int32Value
    def __init__(self, transaction_hash: _Optional[str] = ..., is_registered: bool = ..., sent_code_type: _Optional[int] = ..., code_expiration_date: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., next_send_code_type: _Optional[int] = ..., next_send_code_wait_time: _Optional[_Union[_collections_pb2.Int64Value, _Mapping]] = ..., code_timeout: _Optional[_Union[_collections_pb2.Int32Value, _Mapping]] = ...) -> None: ...

class Auth(_message.Message):
    __slots__ = ("user", "jwt")
    USER_FIELD_NUMBER: _ClassVar[int]
    JWT_FIELD_NUMBER: _ClassVar[int]
    user: _users_pb2.User
    jwt: _collections_pb2.StringValue
    def __init__(self, user: _Optional[_Union[_users_pb2.User, _Mapping]] = ..., jwt: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...
