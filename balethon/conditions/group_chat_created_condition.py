from .condition import Condition


@Condition.create
async def group_chat_created(condition, client, message) -> bool:
    return bool(message.group_chat_created)
