from .condition import Condition


@Condition.create
async def new_chat_members(condition, client, message) -> bool:
    return bool(message.new_chat_members)
