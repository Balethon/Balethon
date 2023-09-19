from .condition import Condition


@Condition.create
async def supergroup_chat_created(condition, client, message):
    return bool(message.supergroup_chat_created)
