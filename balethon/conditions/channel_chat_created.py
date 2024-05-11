from .condition import Condition


@Condition.create
def channel_chat_created(event) -> bool:
    return bool(event.channel_chat_created)
