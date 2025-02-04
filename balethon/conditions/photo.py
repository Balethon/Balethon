from .condition import create
from ..objects import Message


@create(can_process=Message)
def photo(event) -> bool:
    return bool(event.photo)
