from .condition import Condition


@Condition.create
async def delete_chat_photo(event) -> bool:
    return bool(event.delete_chat_photo)
