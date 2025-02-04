from .condition import create
from ..objects import Message


@create(can_process=Message)
def entities(event) -> bool:
    return bool(event.entities or event.caption_entities)
