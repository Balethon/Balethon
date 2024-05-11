from .condition import Condition


@Condition.create
def all() -> bool:
    return True
