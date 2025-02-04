from .condition import create


@create
def delete_chat_photo(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.delete_chat_photo)
