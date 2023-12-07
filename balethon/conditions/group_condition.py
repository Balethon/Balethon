from .condition import Condition


@Condition.create
async def group(condition, client, message) -> bool:
    return message.chat.type == "group"
