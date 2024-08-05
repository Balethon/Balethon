from .condition import Condition


@Condition.create
def pinned_message(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.pinned_message)
