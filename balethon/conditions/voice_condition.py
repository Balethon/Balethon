from .condition import Condition


@Condition.create
async def voice(condition, client, message):
    return bool(message.voice)
