from .condition import Condition


@Condition.create
async def entities(event) -> bool:
    return bool(event.entities or event.caption_entities)
