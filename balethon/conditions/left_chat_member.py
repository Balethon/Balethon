from .condition import Condition


@Condition.create
def left_chat_member(event) -> bool:
    return bool(event.left_chat_member)
