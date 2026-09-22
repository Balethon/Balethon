from .update_handler import UpdateHandler
from ..objects import Message

try:
    from ..proto.updates import Message as ProtobufMessage
except ImportError:
    class ProtobufMessage:
        pass


class RawMessageHandler(UpdateHandler):
    can_handle = ProtobufMessage

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)

    def handle(self, *args, client=None, event=None, **kwargs):
        if client is not None:
            kwargs["client"] = client
        if event is not None:
            kwargs["message"] = event
        return super().handle(*args, **kwargs)
