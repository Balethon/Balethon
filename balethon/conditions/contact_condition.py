from .condition import Condition


@Condition.create
async def contact(condition, client, message) -> bool:
    return bool(message.contact)
