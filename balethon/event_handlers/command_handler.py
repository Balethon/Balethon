from inspect import getfullargspec, getdoc, signature

from .message_handler import MessageHandler
from ..conditions import command
from ..objects import Message


class CommandHandler(MessageHandler):
    can_handle = Message

    @staticmethod
    def get_min_arguments(callback):
        args, _, __, defaults, *___ = getfullargspec(callback)
        args_count = len(args)
        defaults_count = 0 if defaults is None else len(defaults)
        return args_count - defaults_count

    @staticmethod
    def get_max_arguments(callback):
        args, varargs, *_ = getfullargspec(callback)
        if varargs is not None:
            return None
        return len(args)

    @staticmethod
    def get_help(callback):
        name = callback.__name__
        sig = signature(callback)
        doc = getdoc(callback)
        help = f"/{name}"
        for p in sig.parameters:
            param = sig.parameters[p]
            if param.kind is param.KEYWORD_ONLY:
                continue
            if param.annotation is param.empty:
                param_string = param.name
            else:
                try:
                    annotation = param.annotation.__name__
                except AttributeError:
                    annotation = param.annotation
                param_string = f"{param.name}: {annotation}"
            if param.kind is param.VAR_POSITIONAL:
                help += f" [*{param_string}]"
            elif param.default is param.empty:
                help += f" <{param_string}>"
            else:
                help += f" [{param_string}]"
        if doc:
            help += f"\n{doc}"
        return help

    def __init__(self, callback, condition=None, name=None, min_arguments=None, max_arguments=None):
        if name is None:
            name = callback.__name__
        if min_arguments is None:
            min_arguments = self.get_min_arguments(callback)
        if max_arguments is None:
            max_arguments = self.get_max_arguments(callback)
        self.help = self.get_help(callback)
        command_condition = command(name, min_arguments, max_arguments)
        if condition is None:
            condition = command_condition
        else:
            condition = command_condition & condition
        super().__init__(callback, condition)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["message"] = event
            _, *arguments = event.text.split()
            args += tuple(arguments)
        return super().handle(*args, **kwargs)
