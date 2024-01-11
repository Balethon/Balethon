from .condition import Condition


@Condition.create
async def text(condition, client, message) -> bool:
    return bool(message.text)
