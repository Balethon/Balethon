from .event_handler import EventHandler
from ..objects import CallbackQuery


class CallbackQueryHandler(EventHandler):
    can_handle = CallbackQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
