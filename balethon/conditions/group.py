from .condition import Condition


@Condition.create
async def group(event) -> bool:
    return event.chat.type == "group"
