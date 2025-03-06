from .condition import create
from ..objects import Message, CallbackQuery
from ..enums import ChatType


@create(can_process=(Message, CallbackQuery))
def channel(event) -> bool:
    if isinstance(event, Message):
        return event.chat.type == ChatType.CHANNEL
    elif isinstance(event, CallbackQuery):
        return event.message.chat.type == ChatType.CHANNEL
