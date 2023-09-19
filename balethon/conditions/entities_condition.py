from .condition import Condition


@Condition.create
async def entities(condition, client, message):
    return bool(message.entities or message.caption_entities)
