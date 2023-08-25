from .event_handler import EventHandler


class MessageHandler(EventHandler):

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
