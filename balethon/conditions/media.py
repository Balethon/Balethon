from .condition import Condition


@Condition.create
def media(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.animation or event.audio or event.document or event.photo or event.video or event.voice)
