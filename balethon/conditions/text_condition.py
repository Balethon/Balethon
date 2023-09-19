from .condition import Condition


@Condition.create
async def text(condition, client, message):
    return bool(message.text)
