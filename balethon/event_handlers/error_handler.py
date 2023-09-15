from .event_handler import EventHandler


class ErrorHandler(EventHandler):
    can_handle = Exception

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
