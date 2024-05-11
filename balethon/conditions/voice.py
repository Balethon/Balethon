from .condition import Condition


@Condition.create
def voice(event) -> bool:
    return bool(event.voice)
