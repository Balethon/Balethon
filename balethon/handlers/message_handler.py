from .handler import Handler


class MessageHandler(Handler):

    def __init__(self, callback, condition=None):
        super().__init__(callback, condition)
