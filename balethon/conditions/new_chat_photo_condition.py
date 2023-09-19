from .condition import Condition


@Condition.create
async def new_chat_photo(condition, client, message):
    return bool(message.new_chat_photo)
