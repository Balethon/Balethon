from .condition import Condition


@Condition.create
async def caption(condition, client, message) -> bool:
    return bool(message.caption)
