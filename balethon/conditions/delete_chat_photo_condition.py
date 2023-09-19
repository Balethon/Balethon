from .condition import Condition


@Condition.create
async def delete_chat_photo(condition, client, message):
    return bool(message.delete_chat_photo)
