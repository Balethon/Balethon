from .update_handler import UpdateHandler
from ..objects import ShippingQuery


class ShippingQueryHandler(UpdateHandler):
    can_handle = ShippingQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def __call__(self, client=None, shipping_query=None, *args, **kwargs):
        return super().__call__(*args, client=client, shipping_query=shipping_query, **kwargs)
