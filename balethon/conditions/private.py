from .condition import Condition


@Condition.create
async def private(event) -> bool:
    return event.chat.type == "private"
