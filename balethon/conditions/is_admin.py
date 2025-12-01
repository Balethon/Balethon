from typing import Union, Tuple

from .is_joined import IsJoined
from ..enums import ChatMemberStatus


class IsAdmin(IsJoined):
    ACCEPTED_STATUSES = ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR

    def __init__(
            self,
            *chat_ids: Union[int, str],
            accepted_statuses: Tuple[str, ...] = None,
            source_chat: bool = False
    ):
        super().__init__(*chat_ids, accepted_statuses=accepted_statuses)
        self.source_chat = source_chat
