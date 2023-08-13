from .event_handler import EventHandler


class MessageEventHandler(EventHandler):

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
