from .condition import create
from ..objects import Message, CallbackQuery
from ..enums import ChatType


@create(can_process=(Message, CallbackQuery))
def group(event) -> bool:
    if isinstance(event, Message):
        return event.chat.type == ChatType.GROUP
    elif isinstance(event, CallbackQuery):
        return event.message.chat.type == ChatType.GROUP
