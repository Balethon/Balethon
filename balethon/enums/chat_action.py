from enum import auto

from .name_enum import NameEnum
from balethon.proto import enums


class ChatAction(NameEnum):
    TYPING = auto()
    UPLOAD_PHOTO = auto()
    RECORD_VIDEO = auto()
    UPLOAD_VIDEO = auto()
    CHOOSE_STICKER = auto()
    UPLOAD_VOICE = auto()
    RECORD_VOICE = auto()

    def to_protobuf(self):
        if self is ChatAction.TYPING:
            return enums.TYPING_TYPE_TEXT
        if self is ChatAction.UPLOAD_PHOTO:
            return enums.TYPING_TYPE_SENDING_PHOTO
        if self is ChatAction.RECORD_VIDEO:
            return enums.TYPING_TYPE_SENDING_VIDEO
        if self is ChatAction.UPLOAD_VIDEO:
            return enums.TYPING_TYPE_SENDING_VIDEO
        if self is ChatAction.CHOOSE_STICKER:
            return enums.TYPING_TYPE_CHOOSING_STICKER
        if self is ChatAction.UPLOAD_VOICE:
            return enums.TYPING_TYPE_SENDING_VOICE
        if self is ChatAction.RECORD_VOICE:
            return enums.TYPING_TYPE_SENDING_VOICE
        return enums.TYPING_TYPE_UNKNOWN
