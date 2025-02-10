from typing import Union, Tuple

from .condition import Condition
from ..objects import Message, CallbackQuery
from ..errors import RPCError, ForbiddenError


class IsJoined(Condition):
    ACCEPTED_STATUSES = ("member", "administrator", "creator")

    def __init__(self, *chat_ids: Union[int, str], accepted_statuses: Tuple[str, ...] = None):
        super().__init__(can_process=(Message, CallbackQuery))
        self.chat_ids = chat_ids
        self.accepted_statuses = accepted_statuses or self.ACCEPTED_STATUSES

    async def __call__(self, client, event) -> bool:
        if not event.author:
            return False
        for chat_id in self.chat_ids:
            try:
                chat_member = await client.get_chat_member(chat_id, event.author.id)
            except ForbiddenError as error:
                raise error
            except RPCError:
                return False
            else:
                if chat_member.status not in self.ACCEPTED_STATUSES:
                    return False
        return True
