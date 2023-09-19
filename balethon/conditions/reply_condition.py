from .condition import Condition


@Condition.create
async def reply(condition, client, message):
    return bool(message.reply_to_message)
