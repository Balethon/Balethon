from .condition import create


@create
def entities(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.entities or event.caption_entities)
