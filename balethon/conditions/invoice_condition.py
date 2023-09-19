from .condition import Condition


@Condition.create
async def invoice(condition, client, message):
    return bool(message.invoice)
