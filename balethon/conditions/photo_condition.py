from .condition import Condition


@Condition.create
async def photo(condition, client, message):
    return bool(message.photo)
