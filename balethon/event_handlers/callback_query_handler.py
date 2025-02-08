from .update_handler import UpdateHandler
from ..objects import CallbackQuery


class CallbackQueryHandler(UpdateHandler):
    can_handle = CallbackQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["callback_query"] = event
        return super().handle(*args, **kwargs)
