from .condition import Condition


@Condition.create
async def left_chat_member(event) -> bool:
    return bool(event.left_chat_member)
