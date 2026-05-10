from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_PRIVATE: _ClassVar[Restriction]
    RESTRICTION_PUBLIC: _ClassVar[Restriction]

class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUP_TYPE_GROUP: _ClassVar[GroupType]
    GROUP_TYPE_CHANNEL: _ClassVar[GroupType]
    GROUP_TYPE_SUPER_GROUP: _ClassVar[GroupType]
RESTRICTION_PRIVATE: Restriction
RESTRICTION_PUBLIC: Restriction
GROUP_TYPE_GROUP: GroupType
GROUP_TYPE_CHANNEL: GroupType
GROUP_TYPE_SUPER_GROUP: GroupType
