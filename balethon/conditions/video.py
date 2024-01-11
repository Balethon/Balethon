from .condition import Condition


@Condition.create
async def video(condition, client, message) -> bool:
    return bool(message.video)
