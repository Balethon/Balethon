from .condition import create
from ..objects import Message


@create(can_process=Message)
def document(event) -> bool:
    return bool(event.document)
