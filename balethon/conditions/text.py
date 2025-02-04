from .condition import create
from ..objects import Message


@create(can_process=Message)
def text(event) -> bool:
    return bool(event.text)
