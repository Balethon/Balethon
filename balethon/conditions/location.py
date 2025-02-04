from .condition import create
from ..objects import Message


@create(can_process=Message)
def location(event) -> bool:
    return bool(event.location)
