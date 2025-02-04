from .condition import create


@create
def photo(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.photo)
