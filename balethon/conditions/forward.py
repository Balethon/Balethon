from .condition import create
from ..objects import Message


@create(can_process=Message)
def forward(event) -> bool:
    return bool(event.forward_from or event.forward_from_chat)
