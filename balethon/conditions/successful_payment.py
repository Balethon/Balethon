from .condition import Condition


@Condition.create
async def successful_payment(event) -> bool:
    return bool(event.successful_payment)
