from .condition import create


@create
def channel(event) -> bool:
    from ..objects import Message, CallbackQuery
    if isinstance(event, Message):
        event = event.chat.type
    elif isinstance(event, CallbackQuery):
        event = event.message.chat.type
    return event == "channel"
