from .condition import Condition


@Condition.create
async def all(condition, client, message):
    return True
