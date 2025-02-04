from .condition import create
from ..objects import Message


@create(can_process=Message)
def group_chat_created(event) -> bool:
    return bool(event.group_chat_created)
