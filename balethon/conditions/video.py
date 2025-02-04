from .condition import create
from ..objects import Message


@create(can_process=Message)
def video(event) -> bool:
    return bool(event.video)
