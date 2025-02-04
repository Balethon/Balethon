from .condition import create


@create
def media_group(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.media_group_id)
