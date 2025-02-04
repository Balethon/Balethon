from .condition import create
from ..objects import Message, CallbackQuery


@create(can_process=(Message, CallbackQuery))
def private(event) -> bool:
    if isinstance(event, Message):
        return event.chat.type == "private"
    elif isinstance(event, CallbackQuery):
        return event.message.chat.type == "private"
