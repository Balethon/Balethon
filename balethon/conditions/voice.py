from .condition import create
from ..objects import Message


@create(can_process=Message)
def voice(event) -> bool:
    return bool(event.voice)
