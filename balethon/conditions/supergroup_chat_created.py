from .condition import Condition


@Condition.create
def supergroup_chat_created(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.supergroup_chat_created)
