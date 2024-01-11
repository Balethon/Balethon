from .condition import Condition


@Condition.create
async def invoice(condition, client, message) -> bool:
    return bool(message.invoice)
