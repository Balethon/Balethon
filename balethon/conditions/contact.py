from .condition import create


@create
def contact(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.contact)
