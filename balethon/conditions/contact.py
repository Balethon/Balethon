from .condition import Condition


@Condition.create
def contact(event) -> bool:
    return bool(event.contact)
