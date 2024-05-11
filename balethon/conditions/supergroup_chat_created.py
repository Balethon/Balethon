from .condition import Condition


@Condition.create
def supergroup_chat_created(event) -> bool:
    return bool(event.supergroup_chat_created)
