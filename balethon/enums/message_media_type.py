from enum import auto

from .name_enum import NameEnum


class MessageMediaType(NameEnum):
    PHOTO = auto()
    VOICE = auto()
    AUDIO = auto()
    VIDEO = auto()
    ANIMATION = auto()
    CONTACT = auto()
    LOCATION = auto()
    STICKER = auto()
    DOCUMENT = auto()
