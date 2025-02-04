from .condition import create
from ..objects import Message


@create(can_process=Message)
def new_chat_photo(event) -> bool:
    return bool(event.new_chat_photo)
