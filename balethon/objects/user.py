from typing import Union

from . import Object
from ..states import StateMachine
from ..sync_support import add_sync_support_to_object


@add_sync_support_to_object
class User(Object):

    def __init__(
            self,
            id: int = None,
            username: str = None,
            first_name: str = None,
            last_name: str = None,
            language_code: str = None,
            is_bot: bool = None,
            **kwargs
    ):
        super().__init__(**kwargs)
        self.id: int = id
        self.username: str = username
        self.first_name: str = first_name
        self.last_name: str = last_name
        self.language_code: str = language_code
        self.is_bot: bool = is_bot

    def mention(self, text=None):
        text = text or self.full_name
        return f"[{text}](https://web.bale.ai/chat?uid={self.id})"

    @property
    def full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        if self.first_name:
            return self.first_name
        return ""

    def set_state(self, state):
        StateMachine.global_state_machine[self.id] = state

    def get_state(self):
        return StateMachine.global_state_machine[self.id]

    def del_state(self):
        del StateMachine.global_state_machine[self.id]

    async def invite(self, chat_id: Union[int, str]):
        return await self.client.invite_user(chat_id, self.id)
