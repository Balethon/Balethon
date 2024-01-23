from .condition import Condition


@Condition.create
async def caption(condition, client, event) -> bool:
    return bool(event.caption)
