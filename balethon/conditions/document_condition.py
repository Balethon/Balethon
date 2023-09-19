from .condition import Condition


@Condition.create
async def document(condition, client, message):
    return bool(message.document)
