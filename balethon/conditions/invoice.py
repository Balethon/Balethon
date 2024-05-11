from .condition import Condition


@Condition.create
def invoice(event) -> bool:
    return bool(event.invoice)
