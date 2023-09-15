from .update_handler import UpdateHandler
from ..objects import CallbackQuery


class CallbackQueryHandler(UpdateHandler):
    can_handle = CallbackQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
