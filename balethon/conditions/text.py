from .condition import Condition


@Condition.create
def text(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.text)
