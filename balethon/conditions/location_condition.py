from .condition import Condition


@Condition.create
async def location(condition, client, message):
    return bool(message.location)
