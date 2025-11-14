from enum import auto

from .name_enum import NameEnum


class TransactionStatus(NameEnum):
    PENDING = auto()
    PAID = auto()
    FAILED = auto()
    REJECTED = auto()
