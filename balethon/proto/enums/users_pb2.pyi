from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Sex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEX_UNKNOWN: _ClassVar[Sex]
    SEX_MALE: _ClassVar[Sex]
    SEX_FEMALE: _ClassVar[Sex]
SEX_UNKNOWN: Sex
SEX_MALE: Sex
SEX_FEMALE: Sex
