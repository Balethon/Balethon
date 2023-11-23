from .condition import Condition


@Condition.create
async def delete_chat_photo(condition, client, message) -> bool:
    return bool(message.delete_chat_photo)
