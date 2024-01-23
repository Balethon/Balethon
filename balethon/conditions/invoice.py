from .condition import Condition


@Condition.create
async def invoice(event) -> bool:
    return bool(event.invoice)
