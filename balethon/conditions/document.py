from .condition import Condition


@Condition.create
async def document(event) -> bool:
    return bool(event.document)
