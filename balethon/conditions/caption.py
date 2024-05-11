from .condition import Condition


@Condition.create
def caption(event) -> bool:
    return bool(event.caption)
