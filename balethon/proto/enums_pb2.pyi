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

class Restriction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RESTRICTION_PRIVATE: _ClassVar[Restriction]
    RESTRICTION_PUBLIC: _ClassVar[Restriction]

class GroupType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    GROUP_TYPE_GROUP: _ClassVar[GroupType]
    GROUP_TYPE_CHANNEL: _ClassVar[GroupType]
    GROUP_TYPE_SUPER_GROUP: _ClassVar[GroupType]

class ExPeerType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    EX_PEER_TYPE_UNKNOWN: _ClassVar[ExPeerType]
    EX_PEER_TYPE_PRIVATE: _ClassVar[ExPeerType]
    EX_PEER_TYPE_GROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_CHANNEL: _ClassVar[ExPeerType]
    EX_PEER_TYPE_BOT: _ClassVar[ExPeerType]
    EX_PEER_TYPE_SUPERGROUP: _ClassVar[ExPeerType]
    EX_PEER_TYPE_THREAD: _ClassVar[ExPeerType]

class TypingType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    TYPING_TYPE_UNKNOWN: _ClassVar[TypingType]
    TYPING_TYPE_TEXT: _ClassVar[TypingType]
    TYPING_TYPE_VOICE_RECORDING: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_VOICE: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_FILE: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_PHOTO: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_VIDEO: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_MUSIC: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_STICKER: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_GIF: _ClassVar[TypingType]
    TYPING_TYPE_CREATING_GIFT_PACKET: _ClassVar[TypingType]
    TYPING_TYPE_SENDING_ALBUM: _ClassVar[TypingType]
    TYPING_TYPE_CHOOSING_EMOJI: _ClassVar[TypingType]

class Sex(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    SEX_UNKNOWN: _ClassVar[Sex]
    SEX_MALE: _ClassVar[Sex]
    SEX_FEMALE: _ClassVar[Sex]
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
RESTRICTION_PRIVATE: Restriction
RESTRICTION_PUBLIC: Restriction
GROUP_TYPE_GROUP: GroupType
GROUP_TYPE_CHANNEL: GroupType
GROUP_TYPE_SUPER_GROUP: GroupType
EX_PEER_TYPE_UNKNOWN: ExPeerType
EX_PEER_TYPE_PRIVATE: ExPeerType
EX_PEER_TYPE_GROUP: ExPeerType
EX_PEER_TYPE_CHANNEL: ExPeerType
EX_PEER_TYPE_BOT: ExPeerType
EX_PEER_TYPE_SUPERGROUP: ExPeerType
EX_PEER_TYPE_THREAD: ExPeerType
TYPING_TYPE_UNKNOWN: TypingType
TYPING_TYPE_TEXT: TypingType
TYPING_TYPE_VOICE_RECORDING: TypingType
TYPING_TYPE_SENDING_VOICE: TypingType
TYPING_TYPE_SENDING_FILE: TypingType
TYPING_TYPE_SENDING_PHOTO: TypingType
TYPING_TYPE_SENDING_VIDEO: TypingType
TYPING_TYPE_SENDING_MUSIC: TypingType
TYPING_TYPE_CHOOSING_STICKER: TypingType
TYPING_TYPE_CHOOSING_GIF: TypingType
TYPING_TYPE_CREATING_GIFT_PACKET: TypingType
TYPING_TYPE_SENDING_ALBUM: TypingType
TYPING_TYPE_CHOOSING_EMOJI: TypingType
SEX_UNKNOWN: Sex
SEX_MALE: Sex
SEX_FEMALE: Sex
