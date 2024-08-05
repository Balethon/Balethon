from .condition import Condition


@Condition.create
def video(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.video)
