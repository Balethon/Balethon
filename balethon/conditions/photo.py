from .condition import Condition


@Condition.create
async def photo(condition, client, message) -> bool:
    return bool(message.photo)
