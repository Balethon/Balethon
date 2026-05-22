from enum import auto

from .name_enum import NameEnum


class PeerType(NameEnum):
    USER = auto()
    CHANNEL = auto()
