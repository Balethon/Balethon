from .condition import Condition


@Condition.create
def group_chat_created(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.group_chat_created)
