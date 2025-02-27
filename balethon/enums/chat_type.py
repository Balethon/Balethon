from enum import auto

from .name_enum import NameEnum


class ChatType(NameEnum):
    PRIVATE = auto()
    GROUP = auto()
    CHANNEL = auto()
