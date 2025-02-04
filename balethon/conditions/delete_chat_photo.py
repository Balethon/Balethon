from .condition import create
from ..objects import Message


@create(can_process=Message)
def delete_chat_photo(event) -> bool:
    return bool(event.delete_chat_photo)
