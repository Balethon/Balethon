from .condition import Condition


@Condition.create
async def text(event) -> bool:
    return bool(event.text)
