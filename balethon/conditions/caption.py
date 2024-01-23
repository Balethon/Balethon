from .condition import Condition


@Condition.create
async def caption(event) -> bool:
    return bool(event.caption)
