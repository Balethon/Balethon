from .condition import create
from ..objects import Message


@create(can_process=Message)
def content(event) -> bool:
    return bool(event.content)
