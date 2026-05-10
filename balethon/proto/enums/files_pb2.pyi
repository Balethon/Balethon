from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class SendType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEND_TYPE_UNKNOWN: _ClassVar[SendType]
    SEND_TYPE_PHOTO: _ClassVar[SendType]
    SEND_TYPE_VIDEO: _ClassVar[SendType]
    SEND_TYPE_VOICE: _ClassVar[SendType]
    SEND_TYPE_GIF: _ClassVar[SendType]
    SEND_TYPE_AUDIO: _ClassVar[SendType]
    SEND_TYPE_DOCUMENT: _ClassVar[SendType]
    SEND_TYPE_STICKER: _ClassVar[SendType]
    SEND_TYPE_CROWDFUNDING: _ClassVar[SendType]
    SEND_TYPE_SPONSORED: _ClassVar[SendType]
SEND_TYPE_UNKNOWN: SendType
SEND_TYPE_PHOTO: SendType
SEND_TYPE_VIDEO: SendType
SEND_TYPE_VOICE: SendType
SEND_TYPE_GIF: SendType
SEND_TYPE_AUDIO: SendType
SEND_TYPE_DOCUMENT: SendType
SEND_TYPE_STICKER: SendType
SEND_TYPE_CROWDFUNDING: SendType
SEND_TYPE_SPONSORED: SendType
