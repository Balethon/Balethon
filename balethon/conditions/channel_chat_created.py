from .condition import Condition


@Condition.create
def channel_chat_created(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.channel_chat_created)
