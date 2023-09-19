from .condition import Condition


@Condition.create
async def pinned_message(condition, client, message):
    return bool(message.pinned_message)
