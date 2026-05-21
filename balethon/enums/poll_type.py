from enum import auto

from .name_enum import NameEnum


class PollType(NameEnum):
    REGULAR = auto()
    QUIZ = auto()
