from ..structs import collections_pb2 as _collections_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StartPhoneAuth(_message.Message):
    __slots__ = ("phone_number", "app_id", "api_key", "device_hash", "device_title", "send_code_type")
    PHONE_NUMBER_FIELD_NUMBER: _ClassVar[int]
    APP_ID_FIELD_NUMBER: _ClassVar[int]
    API_KEY_FIELD_NUMBER: _ClassVar[int]
    DEVICE_HASH_FIELD_NUMBER: _ClassVar[int]
    DEVICE_TITLE_FIELD_NUMBER: _ClassVar[int]
    SEND_CODE_TYPE_FIELD_NUMBER: _ClassVar[int]
    phone_number: int
    app_id: int
    api_key: str
    device_hash: str
    device_title: str
    send_code_type: int
    def __init__(self, phone_number: _Optional[int] = ..., app_id: _Optional[int] = ..., api_key: _Optional[str] = ..., device_hash: _Optional[str] = ..., device_title: _Optional[str] = ..., send_code_type: _Optional[int] = ...) -> None: ...

class ValidateCode(_message.Message):
    __slots__ = ("transaction_hash", "code", "is_jwt")
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    IS_JWT_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: str
    code: str
    is_jwt: _collections_pb2.BoolValue
    def __init__(self, transaction_hash: _Optional[str] = ..., code: _Optional[str] = ..., is_jwt: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class ValidatePassword(_message.Message):
    __slots__ = ("transaction_hash", "password", "is_jwt")
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    IS_JWT_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: str
    password: str
    is_jwt: _collections_pb2.BoolValue
    def __init__(self, transaction_hash: _Optional[str] = ..., password: _Optional[str] = ..., is_jwt: _Optional[_Union[_collections_pb2.BoolValue, _Mapping]] = ...) -> None: ...

class SignUp(_message.Message):
    __slots__ = ("transaction_hash", "name", "sex", "password")
    TRANSACTION_HASH_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SEX_FIELD_NUMBER: _ClassVar[int]
    PASSWORD_FIELD_NUMBER: _ClassVar[int]
    transaction_hash: str
    name: str
    sex: int
    password: _collections_pb2.StringValue
    def __init__(self, transaction_hash: _Optional[str] = ..., name: _Optional[str] = ..., sex: _Optional[int] = ..., password: _Optional[_Union[_collections_pb2.StringValue, _Mapping]] = ...) -> None: ...

class TerminateAllSessions(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...

class GetJWTToken(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
