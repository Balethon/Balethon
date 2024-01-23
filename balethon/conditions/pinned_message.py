from .condition import Condition


@Condition.create
async def pinned_message(event) -> bool:
    return bool(event.pinned_message)
