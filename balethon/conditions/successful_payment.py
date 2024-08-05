from .condition import Condition


@Condition.create
def successful_payment(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.successful_payment)
