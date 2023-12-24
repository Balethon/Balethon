from .update_handler import UpdateHandler
from ..objects import CallbackQuery


class CallbackQueryHandler(UpdateHandler):
    can_handle = CallbackQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def __call__(self, client=None, callback_query=None, *args, **kwargs):
        return super().__call__(*args, client=client, callback_query=callback_query, **kwargs)
