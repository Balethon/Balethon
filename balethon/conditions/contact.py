from .condition import create
from ..objects import Message


@create(can_process=Message)
def contact(event) -> bool:
    return bool(event.contact)
