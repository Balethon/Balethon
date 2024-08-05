from .condition import Condition


@Condition.create
def photo(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.photo)
