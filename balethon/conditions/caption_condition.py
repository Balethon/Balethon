from .condition import Condition


@Condition.create
async def caption(condition, client, message):
    return bool(message.caption)
