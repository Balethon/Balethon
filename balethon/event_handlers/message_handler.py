from .event_handler import EventHandler
from ..objects import Message


class MessageHandler(EventHandler):
    can_handle = Message

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
