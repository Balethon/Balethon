from .message_handler import MessageHandler
from ..conditions import text, command
from ..objects import Message


class CommandHandler(MessageHandler):
    can_handle = Message

    def __init__(self, callback, condition=None, name=None):
        if name is None:
            name = callback.__name__
        command_condition = command(name)
        if condition is None:
            condition = text & command_condition
        else:
            condition = text & command_condition & condition
        super().__init__(callback, condition)

    def __call__(self, client=None, message=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if message is not None:
            kwargs["message"] = message
        return super().__call__(*args, **kwargs)
