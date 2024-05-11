from .condition import Condition


@Condition.create
def pinned_message(event) -> bool:
    return bool(event.pinned_message)
