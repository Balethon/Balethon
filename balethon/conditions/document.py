from .condition import Condition


@Condition.create
def document(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.document)
