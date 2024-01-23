from .condition import Condition


@Condition.create
async def group_chat_created(event) -> bool:
    return bool(event.group_chat_created)
