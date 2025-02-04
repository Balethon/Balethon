from .condition import create
from ..objects import Message


@create(can_process=Message)
def successful_payment(event) -> bool:
    return bool(event.successful_payment)
