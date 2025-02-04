from .condition import Condition
from ..objects import Message, CallbackQuery


class Chat(Condition):
    def __init__(self, *chats):
        super().__init__(can_process=(Message, CallbackQuery))
        self.chats = set(chats)

    async def __call__(self, client, event) -> bool:
        if isinstance(event, Message):
            return event.chat.id in self.chats
        elif isinstance(event, CallbackQuery):
            return event.message.chat.id in self.chats
