from .condition import Condition


@Condition.create
async def voice(event) -> bool:
    return bool(event.voice)
