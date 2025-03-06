from typing import Union, Tuple

from .condition import Condition
from ..objects import Message, CallbackQuery
from ..enums import ChatMemberStatus
from ..errors import RPCError, ForbiddenError


class IsJoined(Condition):
    ACCEPTED_STATUSES = ChatMemberStatus.MEMBER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.CREATOR

    def __init__(self, *chat_ids: Union[int, str], accepted_statuses: Tuple[str, ...] = None):
        super().__init__(can_process=(Message, CallbackQuery))
        self.chat_ids = list(chat_ids)
        self.chats = []
        self.accepted_statuses = accepted_statuses or self.ACCEPTED_STATUSES

    async def update_chats(self, client):
        self.chats = []
        for chat_id in self.chat_ids:
            chat = await client.get_chat(chat_id)
            self.chats.append(chat)
        self.chat_ids = [chat.id for chat in self.chats]

    async def __call__(self, client, event) -> bool:
        if not self.chats:
            await self.update_chats(client)
        if not event.author:
            return False
        event.not_joined_chats = []
        for chat in self.chats:
            try:
                chat_member = await client.get_chat_member(chat.id, event.author.id)
            except ForbiddenError as error:
                raise error
            except RPCError:
                event.not_joined_chats.append(chat)
            else:
                if chat_member.status not in self.accepted_statuses:
                    event.not_joined_chats.append(chat)
        return not bool(event.not_joined_chats)
