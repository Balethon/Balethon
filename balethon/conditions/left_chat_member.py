from .condition import create
from ..objects import Message


@create(can_process=Message)
def left_chat_member(event) -> bool:
    return bool(event.left_chat_member)
