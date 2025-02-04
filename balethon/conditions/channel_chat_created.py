from .condition import create


@create
def channel_chat_created(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.channel_chat_created)
