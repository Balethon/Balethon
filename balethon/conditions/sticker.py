from .condition import create
from ..objects import Message


@create(can_process=Message)
def sticker(event) -> bool:
    return bool(event.sticker)
