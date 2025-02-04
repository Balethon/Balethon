from .condition import create
from ..objects import Message


@create(can_process=Message)
def invoice(event) -> bool:
    return bool(event.invoice)
