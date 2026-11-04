from enum import auto

from .name_enum import NameEnum


class ButtonStyle(NameEnum):
    PRIMARY = auto()
    SUCCESS = auto()
    DANGER = auto()
