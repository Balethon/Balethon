from .update_handler import UpdateHandler
from ..objects import EditedMessage


class EditedMessageHandler(UpdateHandler):
    can_handle = EditedMessage

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def __call__(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["edited_message"] = event
        return super().__call__(*args, **kwargs)
