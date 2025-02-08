from .update_handler import UpdateHandler
from ..objects import PreCheckoutQuery


class PreCheckoutQueryHandler(UpdateHandler):
    can_handle = PreCheckoutQuery

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["pre_checkout_query"] = event
        return super().handle(*args, **kwargs)
