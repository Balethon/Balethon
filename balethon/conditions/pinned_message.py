from .condition import create
from ..objects import Message


@create(can_process=Message)
def pinned_message(event) -> bool:
    return bool(event.pinned_message)
