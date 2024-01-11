from .condition import Condition


@Condition.create
async def all(condition, client, message) -> bool:
    return True
