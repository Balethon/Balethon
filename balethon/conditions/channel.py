from .condition import create
from ..objects import Message, CallbackQuery


@create(can_process=(Message, CallbackQuery))
def channel(event) -> bool:
    if isinstance(event, Message):
        return event.chat.type == "channel"
    elif isinstance(event, CallbackQuery):
        return event.message.chat.type == "channel"
