from enum import auto

from .name_enum import NameEnum
from balethon.proto import enums


class ChatType(NameEnum):
    PRIVATE = auto()
    GROUP = auto()
    CHANNEL = auto()
    BOT = auto()

    def to_protobuf(self):
        if self is ChatType.PRIVATE:
            return enums.EX_PEER_TYPE_PRIVATE
        if self is ChatType.GROUP:
            return enums.EX_PEER_TYPE_GROUP
        if self is ChatType.CHANNEL:
            return enums.EX_PEER_TYPE_CHANNEL
        if self is ChatType.BOT:
            return enums.EX_PEER_TYPE_BOT
        return enums.EX_PEER_TYPE_UNKNOWN
