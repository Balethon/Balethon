from .condition import create
from ..objects import Message


@create(can_process=Message)
def number(event) -> bool:
    try:
        int(event.content)
    except ValueError:
        return False
    else:
        return True
