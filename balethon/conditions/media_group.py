from .condition import create
from ..objects import Message


@create(can_process=Message)
def media_group(event) -> bool:
    return bool(event.media_group_id)
