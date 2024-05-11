from .condition import Condition


@Condition.create
def successful_payment(event) -> bool:
    return bool(event.successful_payment)
