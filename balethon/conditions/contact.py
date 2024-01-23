from .condition import Condition


@Condition.create
async def contact(event) -> bool:
    return bool(event.contact)
