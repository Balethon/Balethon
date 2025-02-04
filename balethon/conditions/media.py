from .condition import create
from ..objects import Message


@create(can_process=Message)
def media(event) -> bool:
    return bool(event.animation or event.audio or event.document or event.photo or event.video or event.voice)
