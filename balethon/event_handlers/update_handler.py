from .event_handler import EventHandler
from ..objects import Object


class UpdateHandler(EventHandler):
    can_handle = Object

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
