from .is_joined import IsJoined
from ..enums import ChatMemberStatus


class IsAdmin(IsJoined):
    ACCEPTED_STATUSES = ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR
