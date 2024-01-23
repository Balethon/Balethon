from .condition import Condition


@Condition.create
async def reply(event) -> bool:
    return bool(event.reply_to_message)
