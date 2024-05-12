from .condition import Condition


class Chat(Condition):

    def __init__(self, *chats):
        super().__init__()
        self.chats = set(chats)

    async def __call__(self, client, event) -> bool:
        from ..objects import Message, CallbackQuery
        if isinstance(event, Message):
            event = event.chat.id
        elif isinstance(event, CallbackQuery):
            event = event.message.chat.id
        return event in self.chats
