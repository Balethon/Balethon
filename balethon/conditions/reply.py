from .condition import create


@create
def reply(event) -> bool:
    from ..objects import Message
    if isinstance(event, Message):
        return bool(event.reply_to_message)
