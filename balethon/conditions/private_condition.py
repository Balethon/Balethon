from .condition import Condition


@Condition.create
async def private(condition, client, message):
    return message.chat.type == "private"
