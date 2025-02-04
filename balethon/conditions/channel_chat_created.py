from .condition import create
from ..objects import Message


@create(can_process=Message)
def channel_chat_created(event) -> bool:
    return bool(event.channel_chat_created)
