from .condition import Condition


@Condition.create
async def contact(condition, client, message):
    return bool(message.contact)
