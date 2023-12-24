from .update_handler import UpdateHandler
from ..objects import Message


class EditedMessageHandler(UpdateHandler):
    can_handle = Message

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def __call__(self, client=None, message=None, /, *args, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if message is not None:
            kwargs["message"] = message
        return super().__call__(*args, **kwargs)
