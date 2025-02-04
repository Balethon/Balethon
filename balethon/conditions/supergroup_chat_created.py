from .condition import create
from ..objects import Message


@create(can_process=Message)
def supergroup_chat_created(event) -> bool:
    return bool(event.supergroup_chat_created)
