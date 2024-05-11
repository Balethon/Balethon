from .condition import Condition


@Condition.create
def new_chat_title(event) -> bool:
    return bool(event.new_chat_title)
