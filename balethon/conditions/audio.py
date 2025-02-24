from .condition import create
from ..objects import Message


@create(can_process=Message)
def audio(event) -> bool:
    return bool(event.audio)
