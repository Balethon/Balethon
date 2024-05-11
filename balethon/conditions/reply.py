from .condition import Condition


@Condition.create
def reply(event) -> bool:
    return bool(event.reply_to_message)
