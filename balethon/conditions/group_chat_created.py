from .condition import Condition


@Condition.create
def group_chat_created(event) -> bool:
    return bool(event.group_chat_created)
