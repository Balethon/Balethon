from .structs import collections_pb2 as _collections_pb2
from .structs import set_updates_pb2 as _set_updates_pb2
from .requests import request_pb2 as _request_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientPack(_message.Message):
    __slots__ = ("ws_request", "ping")
    WS_REQUEST_FIELD_NUMBER: _ClassVar[int]
    PING_FIELD_NUMBER: _ClassVar[int]
    ws_request: Request
    ping: Ping
    def __init__(self, ws_request: _Optional[_Union[Request, _Mapping]] = ..., ping: _Optional[_Union[Ping, _Mapping]] = ...) -> None: ...

class Ping(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class Request(_message.Message):
    __slots__ = ("service_name", "method", "payload", "metadata", "index")
    SERVICE_NAME_FIELD_NUMBER: _ClassVar[int]
    METHOD_FIELD_NUMBER: _ClassVar[int]
    PAYLOAD_FIELD_NUMBER: _ClassVar[int]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    service_name: str
    method: str
    payload: bytes
    metadata: _request_pb2.Metadata
    index: int
    def __init__(self, service_name: _Optional[str] = ..., method: _Optional[str] = ..., payload: _Optional[bytes] = ..., metadata: _Optional[_Union[_request_pb2.Metadata, _Mapping]] = ..., index: _Optional[int] = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("error", "response", "index")
    ERROR_FIELD_NUMBER: _ClassVar[int]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    error: Error
    response: bytes
    index: int
    def __init__(self, error: _Optional[_Union[Error, _Mapping]] = ..., response: _Optional[bytes] = ..., index: _Optional[int] = ...) -> None: ...

class Error(_message.Message):
    __slots__ = ("code", "message", "details")
    CODE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    DETAILS_FIELD_NUMBER: _ClassVar[int]
    code: int
    message: str
    details: _collections_pb2.MapValue
    def __init__(self, code: _Optional[int] = ..., message: _Optional[str] = ..., details: _Optional[_Union[_collections_pb2.MapValue, _Mapping]] = ...) -> None: ...

class Update(_message.Message):
    __slots__ = ("update",)
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    update: Event
    def __init__(self, update: _Optional[_Union[Event, _Mapping]] = ...) -> None: ...

class ServerPack(_message.Message):
    __slots__ = ("response", "update")
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    UPDATE_FIELD_NUMBER: _ClassVar[int]
    response: Response
    update: Update
    def __init__(self, response: _Optional[_Union[Response, _Mapping]] = ..., update: _Optional[_Union[Update, _Mapping]] = ...) -> None: ...

class Event(_message.Message):
    __slots__ = ("composed_update",)
    COMPOSED_UPDATE_FIELD_NUMBER: _ClassVar[int]
    composed_update: _set_updates_pb2.ComposedUpdates
    def __init__(self, composed_update: _Optional[_Union[_set_updates_pb2.ComposedUpdates, _Mapping]] = ...) -> None: ...
