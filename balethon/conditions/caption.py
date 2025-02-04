from .condition import create


@create
def caption(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.caption)
