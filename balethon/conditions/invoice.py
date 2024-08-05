from .condition import Condition


@Condition.create
def invoice(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.invoice)
