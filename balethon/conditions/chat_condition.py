from .condition import Condition


class Chat(Condition, set):

    def __init__(self, *chats):
        super().__init__(chats)

    async def __call__(self, client, update):
        from ..objects import Message, CallbackQuery
        if isinstance(update, Message):
            update = update.chat.id
        elif isinstance(update, CallbackQuery):
            update = update.message.chat.id
        return update in self
