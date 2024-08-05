from .condition import Condition


@Condition.create
def left_chat_member(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.left_chat_member)
