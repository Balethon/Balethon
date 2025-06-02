from enum import auto

from .name_enum import NameEnum


class ChatAction(NameEnum):
    TYPING = auto()
    UPLOAD_PHOTO = auto()
    UPLOAD_VIDEO = auto()
    RECORD_VOICE = auto()
