from .condition import Condition


@Condition.create
async def content(event) -> bool:
    return bool(event.content)
