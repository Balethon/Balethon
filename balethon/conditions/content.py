from .condition import Condition


@Condition.create
def content(event) -> bool:
    return bool(event.content)
