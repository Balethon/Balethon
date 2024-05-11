from .condition import Condition


@Condition.create
def media(event) -> bool:
    return bool(event.animation or event.audio or event.document or event.photo or event.video or event.voice)
