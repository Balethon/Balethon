from .condition import Condition


@Condition.create
async def video(condition, client, message):
    return bool(message.video)
