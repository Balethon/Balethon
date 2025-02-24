from .condition import create
from ..objects import Message


@create(can_process=Message)
def animation(event) -> bool:
    return bool(event.animation)
