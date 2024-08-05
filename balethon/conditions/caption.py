from .condition import Condition


@Condition.create
def caption(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.caption)
