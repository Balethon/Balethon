from .condition import Condition


@Condition.create
async def location(event) -> bool:
    return bool(event.location)
