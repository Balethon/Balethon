from ..structs import peers_pb2 as _peers_pb2
from ..structs import files_pb2 as _files_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetNasimFileUploadUrl(_message.Message):
    __slots__ = ("expected_size", "crc", "uid", "name", "mime_type", "ex_peer", "send_type", "chunk_size")
    EXPECTED_SIZE_FIELD_NUMBER: _ClassVar[int]
    CRC_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    MIME_TYPE_FIELD_NUMBER: _ClassVar[int]
    EX_PEER_FIELD_NUMBER: _ClassVar[int]
    SEND_TYPE_FIELD_NUMBER: _ClassVar[int]
    CHUNK_SIZE_FIELD_NUMBER: _ClassVar[int]
    expected_size: int
    crc: int
    uid: int
    name: str
    mime_type: str
    ex_peer: _peers_pb2.ExPeer
    send_type: _files_pb2.SendTypeValue
    chunk_size: int
    def __init__(self, expected_size: _Optional[int] = ..., crc: _Optional[int] = ..., uid: _Optional[int] = ..., name: _Optional[str] = ..., mime_type: _Optional[str] = ..., ex_peer: _Optional[_Union[_peers_pb2.ExPeer, _Mapping]] = ..., send_type: _Optional[_Union[_files_pb2.SendTypeValue, _Mapping]] = ..., chunk_size: _Optional[int] = ...) -> None: ...

class GetNasimFileUrl(_message.Message):
    __slots__ = ("file",)
    FILE_FIELD_NUMBER: _ClassVar[int]
    file: _files_pb2.FileLocation
    def __init__(self, file: _Optional[_Union[_files_pb2.FileLocation, _Mapping]] = ...) -> None: ...
