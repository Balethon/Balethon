from .condition import Condition


@Condition.create
def location(event) -> bool:
    return bool(event.location)
