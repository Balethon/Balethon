from .condition import Condition


@Condition.create
async def media(event) -> bool:
    return bool(
        event.photo or
        event.video or
        event.voice or
        event.document
    )
