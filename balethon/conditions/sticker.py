from .condition import Condition


@Condition.create
def sticker(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.sticker)
