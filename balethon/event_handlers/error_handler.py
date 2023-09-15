from .event_handler import EventHandler


class ErrorHandler(EventHandler):
    can_handle = Exception

    def __init__(self, callback):
        super().__init__(callback)
