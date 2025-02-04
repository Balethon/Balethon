from .condition import create
from ..objects import Message


@create(can_process=Message)
def reply(event) -> bool:
    return bool(event.reply_to_message)
