from .condition import Condition


@Condition.create
def text(event) -> bool:
    return bool(event.text)
