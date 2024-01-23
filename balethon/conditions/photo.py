from .condition import Condition


@Condition.create
async def photo(event) -> bool:
    return bool(event.photo)
