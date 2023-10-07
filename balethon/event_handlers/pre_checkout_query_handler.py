from .update_handler import UpdateHandler
from ..objects import PreCheckoutQuery


class PreCheckoutQueryHandler(UpdateHandler):
    can_handle = PreCheckoutQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
