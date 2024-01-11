from .condition import Condition


@Condition.create
async def voice(condition, client, message) -> bool:
    return bool(message.voice)
