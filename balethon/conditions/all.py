from .condition import Condition


@Condition.create
async def all() -> bool:
    return True
