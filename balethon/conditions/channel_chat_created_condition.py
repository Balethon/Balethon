from .condition import Condition


@Condition.create
async def channel_chat_created(condition, client, message):
    return bool(message.channel_chat_created)
