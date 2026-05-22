from enum import auto

from .name_enum import NameEnum


class ForwardOriginType(NameEnum):
    USER = auto()
    CHANNEL = auto()
