from .condition import create
from ..objects import Message, CallbackQuery


@create(can_process=(Message, CallbackQuery))
def group(event) -> bool:
    if isinstance(event, Message):
        return event.chat.type == "group"
    elif isinstance(event, CallbackQuery):
        return event.message.chat.type == "group"
