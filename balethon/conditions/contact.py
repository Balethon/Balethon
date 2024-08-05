from .condition import Condition


@Condition.create
def contact(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.contact)
