from .condition import create


@create
def location(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.location)
