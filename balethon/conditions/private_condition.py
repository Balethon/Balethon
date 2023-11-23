from .condition import Condition


@Condition.create
async def private(condition, client, message) -> bool:
    return message.chat.type == "private"
