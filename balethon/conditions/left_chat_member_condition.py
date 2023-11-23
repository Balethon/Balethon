from .condition import Condition


@Condition.create
async def left_chat_member(condition, client, message) -> bool:
    return bool(message.left_chat_member)
