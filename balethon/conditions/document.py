from .condition import Condition


@Condition.create
async def document(condition, client, message) -> bool:
    return bool(message.document)
