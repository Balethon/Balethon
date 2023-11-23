from .condition import Condition


@Condition.create
async def location(condition, client, message) -> bool:
    return bool(message.location)
