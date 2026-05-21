from .condition import create
from ..objects import Message


@create(can_process=Message)
def poll(event) -> bool:
    return bool(event.poll)
