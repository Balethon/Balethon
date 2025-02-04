from .condition import create


@create
def content(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.content)
