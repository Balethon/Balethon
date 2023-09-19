from .condition import Condition


@Condition.create
async def media(condition, client, message):
    return bool(
        message.photo or
        message.video or
        message.voice or
        message.document
    )
