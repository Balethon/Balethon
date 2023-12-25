from inspect import getfullargspec

from .message_handler import MessageHandler
from ..conditions import text, command
from ..objects import Message


class CommandHandler(MessageHandler):
    can_handle = Message

    def __init__(self, callback, condition=None, name=None, arguments=None):
        if name is None:
            name = callback.__name__
        if arguments is None:
            args, varargs, __, ___, ____, _____, ______ = getfullargspec(callback)
            if varargs is not None:
                arguments = -1
            else:
                arguments = len(args)
        command_condition = command(name, arguments)
        if condition is None:
            condition = text & command_condition
        else:
            condition = text & command_condition & condition
        super().__init__(callback, condition)

    def __call__(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["message"] = event
            _, *arguments = event.text.split()
            args += tuple(arguments)
        return super().__call__(*args, **kwargs)
