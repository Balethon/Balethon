from .condition import create


@create
def voice(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.voice)
