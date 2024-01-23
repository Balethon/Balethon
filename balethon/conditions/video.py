from .condition import Condition


@Condition.create
async def video(event) -> bool:
    return bool(event.video)
