from .condition import Condition


@Condition.create
async def new_chat_members(event) -> bool:
    return bool(event.new_chat_members)
