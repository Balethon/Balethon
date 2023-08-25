from .event_handler import EventHandler
from ..conditions import Command


class CommandHandler(EventHandler):

    def __init__(self, callback, condition=None, name=None):
        if name is None:
            name = callback.__name__
        command_condition = Command(name)
        if condition is None:
            condition = command_condition
        else:
            condition = command_condition & condition
        super().__init__(callback, condition)
