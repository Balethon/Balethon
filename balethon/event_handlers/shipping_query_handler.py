from .update_handler import UpdateHandler
from ..objects import ShippingQuery


class ShippingQueryHandler(UpdateHandler):
    can_handle = ShippingQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
