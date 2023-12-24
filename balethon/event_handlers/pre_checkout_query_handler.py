from .update_handler import UpdateHandler
from ..objects import PreCheckoutQuery


class PreCheckoutQueryHandler(UpdateHandler):
    can_handle = PreCheckoutQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def __call__(self, client=None, pre_checkout_query=None, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if pre_checkout_query is not None:
            kwargs["pre_checkout_query"] = pre_checkout_query
        return super().__call__(*args, **kwargs)
