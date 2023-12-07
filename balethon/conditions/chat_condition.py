from .condition import Condition


class Chat(Condition):

    def __init__(self, *chats):
        super().__init__()
        self.chats = chats

    async def __call__(self, client, update) -> bool:
        from ..objects import Message, CallbackQuery
        if isinstance(update, Message):
            update = update.chat.id
        elif isinstance(update, CallbackQuery):
            update = update.message.chat.id
        return update in self.chats
