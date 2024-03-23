from .condition import Condition
from ..objects import Message, CallbackQuery


@Condition.create
async def channel(event) -> bool:
    if isinstance(event, Message):
        event = event.chat.type
    elif isinstance(event, CallbackQuery):
        event = event.message.chat.type
    return event == "channel"
